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
    
)
from PySide6.QtCore import (
    Qt,
    QThread,
    Signal,
    QMutex,
    Signal
)
from PySide6.QtGui import (
    QAction,
    QIcon,
    QImage,
    QPixmap,

)

import os
import sys

from src.data_model.stu_attendance_detail_model import StuAttendanceDetailModel
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
<<<<<<< HEAD
from src.data_model.attendance_detail_model import AttendanceDetailModel
=======
>>>>>>> 414d9db09c1ed6c339657fb7b26933b73b2fe16e
from src.data_model.course_detail_model import CourseDetailModel
from src.ui.ui_files.ui_main_window import Ui_MainWindow
import src.ui.ui_files.resources as resources
import cv2
from ultralytics import YOLO
import torch
import config.my_config as my_config
from src.core.face_take import FaceTaker
from src.data_model.qt_data_models import CourseListModel, PersonInfoModel, AbsentTableModel
from src.core.face_detect import FaceDetection   
from src.ui.my_delegates import BtnDelegate 
from src.data_model.course_teacher_table_model import CoursecherTableModel
from src.db.course_dao import CourseDAO
from src.db.attendance_info_dao import AttendanceInfoDAO
<<<<<<< HEAD
import matplotlib
matplotlib.use('QtAgg') 
=======
>>>>>>> 414d9db09c1ed6c339657fb7b26933b73b2fe16e

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

        self.person_info_model = None

        self.stackedWidget.setCurrentIndex(0)

        #statusbar 
        self.status_bar = self.statusBar()
        # 导航栏信息
        self.navaigate_map = {0: f"{self.teacher_name}:课程列表",
                              1: f"{self.teacher_name}:课程列表>考勤详情",
<<<<<<< HEAD
                              2: f"{self.teacher_name}:课程列表>考勤详情>学生考勤信息",
                              3: f"{self.teacher_name}:课程列表>考勤详情>学生考勤信息>学生个人缺勤记录"}
=======
                              2: f"{self.teacher_name}:课程列表>考勤详情>学生考勤信息"}
>>>>>>> 414d9db09c1ed6c339657fb7b26933b73b2fe16e
        self.update_navigation_path(0)
        self.stackedWidget.currentChanged.connect(self.update_navigation_path)

        # 显示当前老师下的课程信息
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

        # 人脸的录入
        self.face_taker = None
        self.cur_face = None

        #人脸的检测
        self.face_detector = None
        self.btn_end_face_detect.clicked.connect(self.end_label_face_detection)



        #左侧功能选项
        self.tree_widget.itemClicked.connect(self.on_tree_widget_clicked)
        
    def update_navigation_path(self, idx):
        self.status_bar.showMessage(self.navaigate_map[idx])
<<<<<<< HEAD


    def show_course_detail(self, row):
        # 进入该课程的详细信息，即时间，出勤率，具体那天的出勤信息
        self.attendance_info_dao = AttendanceInfoDAO(self.db)
        course_name = self.course_teacher_model.data(self.course_teacher_model.index(row, 0), Qt.DisplayRole)
        self.course_detail_model = CourseDetailModel(self.attendance_info_dao, course_name)
        self.table_view_course_detail.setModel(self.course_detail_model)
        self.stackedWidget.setCurrentIndex(1)
        self.show_attendance_detail_delegate = BtnDelegate('查看', self.table_view_course_detail)
        self.show_attendance_detail_delegate.btn_clicked_signal.connect(lambda row: self.show_attendance_detail(row, course_name))
        self.table_view_course_detail.setItemDelegateForColumn(4, self.show_attendance_detail_delegate) 
        for row in range(self.course_detail_model.rowCount()):
            self.table_view_course_detail.openPersistentEditor(
                self.course_detail_model.index(row, 4)
            )   


    def show_attendance_detail(self, row, course_name):
        # 进入考勤的详情界面，显示当前课程这一天每个学生的考勤信息
        date = self.course_detail_model.data(self.course_detail_model.index(row, 0), Qt.DisplayRole)
        self.attendance_detail_model = AttendanceDetailModel(self.attendance_info_dao, course_name, date)
        self.table_view_attendance_detail.setModel(self.attendance_detail_model)
        self.stackedWidget.setCurrentIndex(2)
        self.show_stu_attendance_detail_delegate = BtnDelegate('查看', self.table_view_attendance_detail)
        self.show_stu_attendance_detail_delegate.btn_clicked_signal.connect(lambda row: self.show_stu_attendance_detail(row, course_name))
        self.table_view_attendance_detail.setItemDelegateForColumn(3, self.show_stu_attendance_detail_delegate)
        for row in range(self.attendance_detail_model.rowCount()):
            self.table_view_attendance_detail.openPersistentEditor(
                self.attendance_detail_model.index(row, 3)
            )   

    def show_stu_attendance_detail(self, row, course_name):
        # 进入学生的考勤详情界面，显示当前学生的考勤详情
        stu_id = self.attendance_detail_model.data(self.attendance_detail_model.index(row, 1), Qt.DisplayRole)
        self.stu_attendance_detail_model = StuAttendanceDetailModel(self.attendance_info_dao, stu_id)
        self.table_view_stu_attendance_detail.setModel(self.stu_attendance_detail_model)
        self.stackedWidget.setCurrentIndex(3)

=======


    def show_course_detail(self, row):
        # 进入该课程的详细信息，即时间，出勤率，具体那天的出勤信息
        self.attendance_info_dao = AttendanceInfoDAO(self.db)
        course_name = self.course_teacher_model.data(self.course_teacher_model.index(row, 0), Qt.DisplayRole)
        self.course_detail_model = CourseDetailModel(self.attendance_info_dao, course_name)
        self.table_view_course_detail.setModel(self.course_detail_model)
        self.stackedWidget.setCurrentIndex(1)
        self.show_attendance_detail_delegate = BtnDelegate('查看', self.table_view_course_detail)
        self.show_attendance_detail_delegate.btn_clicked_signal.connect(self.show_attendance_detail)
        self.table_view_course_detail.setItemDelegateForColumn(4, self.show_attendance_detail_delegate) 
        for row in range(self.course_detail_model.rowCount()):
            self.table_view_course_detail.openPersistentEditor(
                self.course_detail_model.index(row, 4)
            )   


    def show_attendance_detail(self, row):
        pass
>>>>>>> 414d9db09c1ed6c339657fb7b26933b73b2fe16e

    def on_tree_widget_clicked(self, item, column):
        item_name = item.text(column)
        if item_name == '切换登陆':
            from src.ui.login_window import LoginWindow
            login_window = LoginWindow(self.db, self)
            login_window.exec_()
        
        elif item_name == '课程信息':
            self.stackedWidget.setCurrentIndex(0)
        
        elif item_name == '返回上一级':
            cur_idx = self.stackedWidget.currentIndex()
            if cur_idx == 0:
                pass
            else:
                self.stackedWidget.setCurrentIndex(cur_idx - 1)


    #更改用户
    def change_user(self, teacher_name, username):
        self.teacher_name = teacher_name
        self.username = username

    def start_show_video(self):
        if self.face_taker is not None:
            return
        self.face_taker = FaceTaker(my_config.VIDEO_PATH)
        self.face_taker.update_frame_signal.connect(self.update_video)
        self.face_taker.select_face_signal.connect(self.face_get)

        self.btn_confirm.clicked.connect(self.confirm_face_taken)
        self.btn_pass.clicked.connect(self.face_taker.resume)

        self.face_taker.start()

    def update_video(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
        self.label_disp_video.setPixmap(pixmap)

    def end_show_video(self):
        if self.face_taker is not None:
            self.face_taker.stop()
            self.face_taker = None
            #每次录入完人脸后，都要将对应的向量数据库进行保存
            self.person_info_model.save_vec_db()

    def end_label_face_detection(self):
        if self.face_detector is not None:
            self.face_detector.stop()
            self.face_detector = None


    def face_get(self, qimage):
        self.cur_face = qimage
        pixmap = QPixmap.fromImage(qimage)
        self.label_face.setPixmap(pixmap)
    
    def closeEvent(self, event):
        self.end_show_video()
        self.end_label_face_detection()
        super().closeEvent(event)
        #记得关闭所有的数据库连接

    def confirm_cur_course(self):
        selected_indexes = self.listview_table_select.selectedIndexes()
        if selected_indexes:
            for index in selected_indexes:
                course_name = self.course_list_model.data(index, Qt.DisplayRole)
                self.label_curtable.setText(f"current table:{course_name}")
                self.course_list_model.cur_course_name = course_name
                # self.person_info_model = PersonInfoModel(self.list_model_tables.conn, self.list_model_tables.cur_table_name)
                # self.table_view_show_stu.setModel(self.person_info_model)
                # #同时创建用于表示缺席的学生列表
                # self.absent_table_model = AbsentTableModel(self.list_model_tables.conn.cursor(), self.list_model_tables.cur_table_name)
                # self.table_view_show_absent.setModel(self.absent_table_model)

    def confirm_face_taken(self):
        #确认录入人脸，先获取人脸的特征
        if self.cur_face is None:
            return
        face_feature = self.face_taker.get_face_feature()
        
        name = self.line_edit_name.text()
        age = self.line_edit_age.text()
        gender = self.line_edit_gender.text()

        if name == "" or age == "" or gender == "":
            #保证输入正确的人脸信息
            print("请输入人脸的相关信息") 
            return
        
        #然后人脸的信息，包括特征传递给数据库对象进行保存
        if self.person_info_model is None:
            QMessageBox.warning(self, "", "请选择数据库", QMessageBox.Ok)
            return 
        
        self.person_info_model.insert_data(name, gender, age, face_feature)

        self.face_taker.resume()
        
        #录取完这张图片后，就禁止再点击录入按钮
        self.cur_face = None


    def create_new_course(self):
        text, ok = QInputDialog.getText(self, '输入表名', '表名', QLineEdit.Normal)
        if ok and text:
            self.course_list_model.create_new_course(text)
        else:
            print('取消新表的创建')

    def delete_course(self):
        selected_indexes = self.listview_table_select.selectedIndexes()
        if len(selected_indexes) != 0:
            for idx in selected_indexes:
                course_name = self.course_list_model.data(idx, Qt.DisplayRole)
                self.course_list_model.delete_course(course_name)

    def detect_face(self):
        #点击检测的开始按钮，开始检测人脸
        if self.face_detector != None:
            return 
        self.face_detector = FaceDetection(my_config.VIDEO_PATH, self.person_info_model)
        self.face_detector.update_frame_signal.connect(self.update_frame_detect)
        self.face_detector.transform_face_ids.connect(self.update_absent)
        
        self.face_detector.transform_face_ids.connect(self.update_absent)
        self.face_detector.start()


    def update_frame_detect(self, frame):
        pixmap = QPixmap.fromImage(frame)
        self.label_disp_video_2.setPixmap(pixmap)

    def update_absent(self, id):
        self.absent_table_model.delete_row(id)


    #选中对应的课程进入人脸录入界面
    def enter_face_collection(self):
        selected_indexes = self.listview_table_select.selectedIndexes()
        if len(selected_indexes) == 0:
            #如果没有选中任何选项
            print('请选择一个课程')
        else:
            for index in selected_indexes:
                course_name = self.course_list_model.data(index, Qt.DisplayRole)
                self.label_curtable.setText(f"current table:{course_name}")
                self.course_name = course_name
                #因为人脸录入的时候需要用到学生列表的model,因此要初始化对应的对象
                self.person_info_model = PersonInfoModel(self.db, self.username, self.course_name)
                self.table_view_show_stu.setModel(self.person_info_model)
                
                self.stackedWidget.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    from src.ui.login_window import LoginWindow

    login_window = LoginWindow()
    login_window.show()

    app.exec()