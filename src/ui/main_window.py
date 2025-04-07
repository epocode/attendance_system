from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QToolBar,
    QDockWidget,
    QStatusBar,
    QInputDialog,
    QLineEdit,
    QMessageBox,
    QFileDialog,
    
)
from PySide6.QtCore import (
    Qt,
    QThread,
    Signal,
    QMutex,
    Signal,
    QTimer
)
from PySide6.QtGui import (
    QAction,
    QIcon,
    QImage,
    QPixmap,
    QPainter
)

import os
import sys

from src.data_model.stu_attendance_detail_model import StuAttendanceDetailModel
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.data_model.attendance_detail_model import AttendanceDetailModel
from src.data_model.course_detail_model import CourseDetailModel
from src.ui.ui_files.ui_main_window import Ui_MainWindow
import src.ui.ui_files.resources_rc as resources
import cv2
from ultralytics import YOLO
import torch
import config.my_config as my_config
from src.core.face_detect import FaceDetection   
from src.ui.my_delegates import BtnDelegate 
from src.data_model.course_teacher_table_model import CoursecherTableModel
from src.db.course_dao import CourseDAO
from src.db.attendance_info_dao import AttendanceInfoDAO
import matplotlib
from src.core.model_preload_thread import ModelPreloadThread
from src.db.stu_course_dao import StuCourseDao
from src.db.student_dao import StudentDAO
from src.data_model.absent_model import AbsentModel
import datetime
matplotlib.use('QtAgg') 

class MainWindow(Ui_MainWindow, QMainWindow):
    """
    进入这个窗口，即表明这是属于某个老师的。因此关于老师的信息保存在该窗口对象中。
    对于学生，因为选择不同的课程会有不同的学生列表，因此学生信息应该临时创建，
    使用table widget的时候，到了对应的table才将model放到view中，切换的时候就要
    从view删除对应的model，因为切换班级的时候，对应的model内容也会改变。
    """
    def __init__(self, teacher_name, teacher_username, db, *args, **kwargs):
        super().__init__(*args, **kwargs)   

        self.setupUi(self)

        #主界面要维护的信息
        self.teacher_name = teacher_name
        self.teacher_username = teacher_username
        self.db = db


        #statusbar 
        self.status_bar = self.statusBar()
        self.show_navi_info_Label = QLabel()
        self.status_bar.addPermanentWidget(self.show_navi_info_Label)
        self.navaigate_map = {'course_info': f"{self.teacher_name}:课程列表",
                              'course_detail': f"{self.teacher_name}:课程列表>考勤详情",
                              'attendance_detail': f"{self.teacher_name}:课程列表>考勤详情>学生考勤信息",
                              'stu_attendance_detail': f"{self.teacher_name}:课程列表>考勤详情>学生考勤信息>学生个人缺勤记录",
                              'execute_attendance': '签到页面'}
        self.page_map = {'course_info': 0, 'course_detail': 1,
                         'attendance_detail':2, 'stu_attendance_detail': 3,
                         'execute_attendance': 4}

        self.dirty_pages = {
            'course_info': False,
            'course_detail': False,
            'attendance_detail': False,
            'stu_attendance_detail': False,
            'execute_attendance': False
        }

        #左侧功能选项
        self.tree_widget.itemClicked.connect(self.on_tree_widget_clicked)
 
        QTimer.singleShot(100, self.delayed_model_init)

        # 进入课程界面
        self.enter_course_info_page()





#------------------------------页面切换代码----------------------------------
    def on_tree_widget_clicked(self, item, column):
        """左侧导航栏的具体切换功能"""
        item_name = item.text(column)
        if item_name == '退出登录':
            from src.ui.login_window import LoginWindow
            
            self.login_window = LoginWindow(self.db)
            self.login_window.show()
            self.close()

        elif item_name == '课程信息':
            self.enter_course_info_page()
        
        elif item_name == '返回上一级':
            cur_idx = self.stackedWidget.currentIndex()
            if cur_idx == 0:
                pass
            elif cur_idx == self.page_map['course_detail']:
                self.enter_course_info_page()
            elif cur_idx == self.page_map['attendance_detail'] or cur_idx == self.page_map['execute_attendance']:
                self.show_course_detail()
            elif cur_idx == self.page_map['stu_attendance_detail']:
                self.show_attendance_detail()
    

#------------------------------课程信息页面----------------------------------
    def enter_course_info_page(self):
        """course_info. <-课程名-操作->"""
        self.course_dao = CourseDAO(self.db, self.teacher_username)
        self.course_teacher_model = CoursecherTableModel(self.course_dao, self.teacher_username)
        self.table_view_course_teacher.setModel(self.course_teacher_model)
        self.course_detail_btn_delegate = BtnDelegate('详情', self.table_view_course_teacher)
        self.course_detail_btn_delegate.btn_clicked_signal.connect(self.show_course_detail)
        self.table_view_course_teacher.setItemDelegateForColumn(1, self.course_detail_btn_delegate)    
        for row in range(self.course_teacher_model.rowCount()):
            self.table_view_course_teacher.openPersistentEditor(
                self.course_teacher_model.index(row, 1)
            )
        self.stackedWidget.setCurrentIndex(self.page_map['course_info'])
        self.show_navi_info_Label.setText(self.navaigate_map['course_info'])

#--------------------------某课程的签到日志页面--------------------------------------
    def show_course_detail(self, row=None):
        """ course_detail.<-日期-总人数- 出勤人数-出勤率-操作->"""
        if row is not None:
            self.attendance_info_dao = AttendanceInfoDAO(self.db)
            course_name = self.course_teacher_model.data(self.course_teacher_model.index(row, 0), Qt.DisplayRole)
            self.course_detail_model = CourseDetailModel(self.attendance_info_dao, course_name)
            self.table_view_course_detail.setModel(self.course_detail_model)
            
            self.show_attendance_detail_delegate = BtnDelegate('查看', self.table_view_course_detail)
            self.show_attendance_detail_delegate.btn_clicked_signal.connect(lambda row: self.show_attendance_detail(row, course_name))
            self.table_view_course_detail.setItemDelegateForColumn(4, self.show_attendance_detail_delegate) 
            for row in range(self.course_detail_model.rowCount()):
                self.table_view_course_detail.openPersistentEditor(
                    self.course_detail_model.index(row, 4)
                )   

            # 绑定考勤按钮对应的槽函数
            self.btn_enter_attendance.clicked.connect(lambda: self.on_btn_enter_attendance_clicked(course_name))
        else:
            if self.dirty_pages['course_detail']:
                self.course_detail_model.refresh()
                self.dirty_pages['course_detail'] = False
        self.stackedWidget.setCurrentIndex(self.page_map['course_detail'])  
        self.show_navi_info_Label.setText(self.navaigate_map['course_detail'])

#---------------------------------考勤界面------------------------------------------
    def on_btn_enter_attendance_clicked(self, course_name=None):
        """进入考勤的界面，初始化考勤所需要的属性，绑定组件对应的槽函数"""
        self.btn_start_detect_face.clicked.connect(lambda:self.on_start_detect_face_clicked(course_name))
        self.btn_end_detect_face.clicked.connect(self.on_end_detect_face_clicked)   

        self.stu_course_dao = StuCourseDao(self.db)
        self.absent_model = AbsentModel(self.stu_course_dao, course_name)
        self.table_view_show_absent.setModel(self.absent_model)

        # 设置combo box内容
        if self.combo_box_video_source.count() == 0:
            self.combo_box_video_source.addItem("摄像头", 0)
            self.combo_box_video_source.addItem("视频文件", 'video_file')
            my_config.VIDEO_PATH = 0
            self.combo_box_video_source.currentIndexChanged.connect(self.on_source_selection_changed)


        self.dirty_pages['course_detail'] = True
        self.stackedWidget.setCurrentIndex(self.page_map['execute_attendance'])
        self.show_navi_info_Label.setText(self.navaigate_map['execute_attendance'])

    def on_source_selection_changed(self, index):
        data = self.combo_box_video_source.itemData(index)

        if data == "video_file":
            file_path, _ = QFileDialog.getOpenFileName(self, "选择视频文件", "", "视频文件(*.mp4 *.avi)")
            if file_path:
                my_config.VIDEO_PATH = file_path
            else:
                self.combo_box_video_source.setCurrentIndex(0)
                my_config.VIDEO_PATH = 0
        else:
            my_config.VIDEO_PATH = 0 
  

#------------------------------某课程某天的签到详情----------------------------------
    def show_attendance_detail(self, row=None, course_name=None):
        # 进入考勤的详情界面，显示当前课程这一天每个学生的考勤信息
        if row is not None:
            date = self.course_detail_model.data(self.course_detail_model.index(row, 0), Qt.DisplayRole)
            self.attendance_detail_model = AttendanceDetailModel(self.attendance_info_dao, course_name, date)
            self.table_view_attendance_detail.setModel(self.attendance_detail_model)

            self.show_stu_attendance_detail_delegate = BtnDelegate('查看', self.table_view_attendance_detail)
            self.show_stu_attendance_detail_delegate.btn_clicked_signal.connect(lambda row: self.show_stu_attendance_detail(row))
            self.table_view_attendance_detail.setItemDelegateForColumn(3, self.show_stu_attendance_detail_delegate)
            for row in range(self.attendance_detail_model.rowCount()):
                self.table_view_attendance_detail.openPersistentEditor(
                    self.attendance_detail_model.index(row, 3)
                )   
        else:
            if self.dirty_pages['attendance_detail']:
                self.attendance_detail_model.refresh()
                self.dirty_pages['attendance_detail'] = False
        self.stackedWidget.setCurrentIndex(self.page_map['attendance_detail'])
        self.show_navi_info_Label.setText(self.navaigate_map['attendance_detail'])

#--------------------------某学生的所有签到日志-------------------------------------------
    def show_stu_attendance_detail(self, row=None):
        # 进入学生的考勤详情界面，显示当前学生的考勤详情
        if row is not None:
            stu_id = self.attendance_detail_model.data(self.attendance_detail_model.index(row, 1), Qt.DisplayRole)
            self.stu_attendance_detail_model = StuAttendanceDetailModel(self.attendance_info_dao, stu_id)
            self.table_view_stu_attendance_detail.setModel(self.stu_attendance_detail_model)
        else:
            if self.dirty_pages['stu_attendance_detail']:
                self.stu_attendance_detail_model.refresh()
                self.dirty_pages['stu_attendance_detail'] = False
        self.stackedWidget.setCurrentIndex(self.page_map['stu_attendance_detail'])
        self.show_navi_info_Label.setText(self.navaigate_map['stu_attendance_detail'])  


#-----------------------人脸识别相关--------------------------------------

    def delayed_model_init(self):
        """加载模型"""
        self.preload_thread = ModelPreloadThread()
        self.preload_thread.preload_finished.connect(self.on_model_preload_finished)
        self.preload_thread.start()
        self.status_bar.showMessage("模型加载中，请稍等...")


    def on_model_preload_finished(self, model):
        """模型加载完成后需要干的事"""
        self.preloaded_model = model
        self.status_bar.showMessage("模型加载完成", 2000)


    def on_start_detect_face_clicked(self, course_name):
        #点击检测的开始按钮，开始检测人脸
        self.course_name = course_name
        self.stu_dao = StudentDAO(self.db)
        self.face_detector = FaceDetection(my_config.VIDEO_PATH, self.preloaded_model, self.stu_dao)
        self.face_detector.update_frame_signal.connect(self.update_frame)
        self.face_detector.transform_face_ids.connect(self.update_absent)
        
        self.absent_stu_set = set()
        for row in range(self.absent_model.rowCount()):
            stu_id = self.absent_model.data(self.absent_model.index(row, 0), Qt.DisplayRole)
            self.absent_stu_set.add(stu_id)

        self.face_detector.start()


    def update_absent(self, id):
        if id  in self.absent_stu_set:
            for row in range(self.absent_model.rowCount()):
                stu_id = self.absent_model.data(self.absent_model.index(row, 0), Qt.DisplayRole)
                if str(stu_id) == str(id):
                    self.absent_model.remove_row(row)
                    self.absent_model.layoutChanged.emit()
                    self.status_bar.showMessage(f"检测到学生{stu_id}，已从缺勤列表中移除")

                    # 在attendance_info_dao中添加考勤记录
                    cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
                    self.attendance_info_dao.add_attendance_info(stu_id, self.course_name, cur_date, True)

                    self.absent_stu_set.remove(id)
                    break

        
    def update_frame(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
        self.label_display_cap.setPixmap(pixmap)

        label_size = self.label_display_cap.size()
        pixmap = QPixmap(label_size)
        pixmap.fill(Qt.black)  # 设置背景色
        # 将QImage转换为QPixmap
        img_pixmap = QPixmap.fromImage(qimage)
        # 等比例缩放图像，保持宽高比
        scaled_pixmap = img_pixmap.scaled(
            label_size, 
            Qt.KeepAspectRatio,  # 保持宽高比
            Qt.SmoothTransformation  # 使用平滑的缩放算法
        )
        painter = QPainter(pixmap)
    
        # 计算在标签中的居中位置
        x = (label_size.width() - scaled_pixmap.width()) // 2
        y = (label_size.height() - scaled_pixmap.height()) // 2
        
        # 在指定位置绘制缩放后的图像
        painter.drawPixmap(x, y, scaled_pixmap)
        painter.end()
        # 设置标签的pixmap
        self.label_display_cap.setPixmap(pixmap)


    def on_end_detect_face_clicked(self):
        """结束人脸检测"""
        try:
            if hasattr(self, 'face_detector') and self.face_detector is not None:
                # 将还没签到的学生信息添加进去
                if hasattr(self, 'absent_model') and self.absent_model is not None:
                    for row in range(self.absent_model.rowCount()):
                        stu_id = self.absent_model.data(self.absent_model.index(row, 0), Qt.DisplayRole)
                        # 检查attendance_info_dao是否初始化
                        if hasattr(self, 'attendance_info_dao') and self.attendance_info_dao is not None:
                            self.attendance_info_dao.add_attendance_info(
                                stu_id, 
                                self.course_name, 
                                datetime.datetime.now().strftime('%Y-%m-%d'), 
                                False
                            )
                
                # 停止检测线程
                self.face_detector.stop()
                self.face_detector = None
                
                # 清除显示
                blank_pixmap = QPixmap(self.label_display_cap.size())
                blank_pixmap.fill(Qt.black)
                self.label_display_cap.setPixmap(blank_pixmap)
                
                QApplication.processEvents()  # 确保UI更新
                # 提示用户
                self.status_bar.showMessage("考勤已结束")
        except Exception as e:
            print(f"结束人脸检测时发生错误: {e}")
    
    def closeEvent(self, event):
        """窗口关闭事件处理"""
        try:
            # 如果人脸检测正在进行，先停止它
            if hasattr(self, 'face_detector') and self.face_detector is not None:
                try:
                    self.face_detector.stop()
                    self.face_detector = None
                except Exception as e:
                    print(f"关闭人脸检测线程时出错: {e}")
            
            # 关闭数据库连接或执行其他清理操作
            if hasattr(self, 'db') and self.db is not None:
                try:
                    # 如果有自定义的关闭方法
                    self.db.close()
                    pass
                except Exception as e:
                    print(f"关闭数据库连接时出错: {e}")
        except Exception as e:
            print(f"程序关闭时发生错误: {e}")
            
        # 调用父类的关闭事件
        super().closeEvent(event)


