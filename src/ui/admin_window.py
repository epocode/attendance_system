from PySide6.QtWidgets import (
    QMainWindow,
    QDialog,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QAbstractItemView,
    QComboBox,
    QStyledItemDelegate,
    QWidget,
    QFileDialog,
    QApplication

)
from PySide6.QtCore import Signal, QTimer, Qt
from PySide6.QtGui import QPixmap, QPainter
from src.ui.my_combo_delegate import MyComboDelegate
from src.ui.ui_files.ui_admin_window import Ui_AdminWindow
from src.db.database import DataBase
from src.db.teacher_dao import TeacherDAO
from src.data_model.teacher_table_model import TeacherTableModel
from src.db.course_dao import CourseDAO
from src.data_model.course_table_model import CourseTableModel
from src.db.student_dao import StudentDAO
from src.data_model.student_table_model import StudentTableModel
from src.core.face_take import FaceTaker
import config.my_config as my_config
from src.core.model_preload_thread import ModelPreloadThread
from src.ui.my_delegates import BtnDelegate
from src.db.stu_course_dao import StuCourseDao
from src.data_model.course_stu_model import CourseStuModel
from src.data_model.course_stu_available_model import CourseStuAvailableModel

class AdminWindow(Ui_AdminWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tree_widget.setCurrentItem(self.tree_widget.topLevelItem(1))
        #当前窗口要维护的信息
        self.db = DataBase()
        self.page_map = {"teacher_page":0, "course_page": 1,
                         "student_page":2, "stu_course_page":3,
                         "enter_stu_page": 4}

        #人脸录入相关
        self.face_taker = None
        self.cur_face = None

        self.btn_start_enter.clicked.connect(self.start_enter_stu_with_face)
        self.btn_end_enter.clicked.connect(self.end_enter_face)
        
        #绑定功能切换
        self.initialized_pages = set()
        self.data_dirty = {
            'teacher_page': False,
            'course_page': False,
            'student_page': False,
            'stu_course_page': False,
        }

        self.stacked_widget.setCurrentIndex(0)
        self.tree_widget.itemClicked.connect(self.on_tree_widget_clicked)

                
        # 初始化界面
        self.setup_ui_components()
        
        # 主界面即老师信息界面
        self.enter_page_teacher()

        QTimer.singleShot(100, self.delayed_model_init)  # 延迟1秒后初始化模型


    def setup_ui_components(self):
        """设置UI组件的初始状态和属性"""
        #状态栏
        self.status_bar = self.statusBar()

        # 初始化视频来源下拉框的内容。
        self.setup_source_combo_box()

    
    #选择视频来源
    def setup_source_combo_box(self):
        self.combo_box_video_source.addItem("摄像头", 0)
        self.combo_box_video_source.addItem("视频文件", 'video_file')
        my_config.VIDEO_PATH = 0
        self.combo_box_video_source.currentIndexChanged.connect(self.on_source_selection_changed)

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
  


#---------------------老师管理相关代码------------------------------------------------------------
    def enter_page_teacher(self):
        """进入老师管理界面"""
        page_key = 'teacher_page'

        # 第一次进入该页面，初始化数据模型
        if page_key not in self.initialized_pages:
            self.initialized_pages.add(page_key)
            self.teacher_dao = TeacherDAO(self.db)
            self.teacher_table_model = TeacherTableModel(self.teacher_dao)
            self.table_view_teachers.setModel(self.teacher_table_model)
            self.table_view_teachers.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.btn_add_teacher.clicked.connect(self.on_add_teacher_clicked)
            self.btn_delete_teacher.clicked.connect(self.on_delete_teacher_clicked)


        elif self.data_dirty[page_key]:
            #如果数据脏了，仅仅刷新数据模型即可
            self.teacher_table_model.refresh()

        # 刷新后当前页面不是脏的
        self.data_dirty[page_key] = False
        self.stacked_widget.setCurrentIndex(self.page_map['teacher_page'])

    def on_add_teacher_clicked(self):
        #创建新的老师信息
        input_dialog = TeacherInputDialog()
        if input_dialog.exec() == QDialog.Accepted:
            res = input_dialog.get_value()
            if len(res) == 0:
                print('请输入正确的老师信息')
                return 
            name = res['name']
            username = res['username']
            pswd = res['pswd']
            if not self.teacher_dao.check_single_username(username):
                print('当前用户名已存在')
                return
            self.teacher_dao.add_new(name, username, pswd)
            print('成功添加新老师')

            # 刷新数据模型并且设置关联页面为脏
            self.teacher_table_model.refresh()
            self.set_page_dirty(['course_page', ['student_page']])
        
    def on_delete_teacher_clicked(self):
        selected_indexes = self.table_view_teachers.selectionModel().selectedRows()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            self.teacher_dao.delete_row(selected_row)
            # 刷新数据模型并且设置关联页面为脏
            self.teacher_table_model.refresh()
            self.set_page_dirty(['course_page', ['student_page']])

#---------------------课程管理相关代码------------------------------------------------------------

    def enter_page_course(self):
        """进入课程管理界面"""
        page_key = 'course_page'
        # 第一次进入该页面，初始化数据模型
        if page_key not in self.initialized_pages:
            self.initialized_pages.add(page_key)
            self.course_dao = CourseDAO(self.db)
            self.course_table_model = CourseTableModel(self.course_dao)
            self.table_view_course.setModel(self.course_table_model)
            self.table_view_course.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.btn_add_course.clicked.connect(self.on_add_course_clicked)
            self.btn_delete_course.clicked.connect(self.on_delete_course_clicked)

        elif self.data_dirty[page_key]:
            #如果数据脏了，仅仅刷新数据模型即可
            self.course_table_model.refresh()
        
        self.data_dirty[page_key] = False  # 刷新后当前页面不是脏的
        self.stacked_widget.setCurrentIndex(self.page_map['course_page'])

    def on_add_course_clicked(self):
        #新增课程
        input_dialog = CourseInputDialog(self.teacher_dao)
        if input_dialog.exec() == QDialog.Accepted:
            res = input_dialog.get_value()
            if len(res) == 0:
                print('请输入正确的课程信息')
                return
            course_name = res['course_name']
            teacher_username = res['teacher_username']
            if not self.course_dao.check_single_course_name(course_name):
                print('当前课程名已经存在')
                return
            self.course_dao.add_new(course_name, teacher_username)
            # 刷新数据模型并且设置关联页面为脏
            self.course_table_model.refresh()
            self.set_page_dirty(['student_page'])
        
    def on_delete_course_clicked(self):
        indexes = self.table_view_course.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            self.course_dao.delete_course_by_row(row)
            # 刷新数据模型并且设置关联页面为脏
            self.course_table_model.refresh()
            self.set_page_dirty(['student_page'])


#---------------------学生管理相关代码------------------------------------------------------------
    def enter_page_student(self):
        """进入学生管理界面，记住，该界面还包括显示学生课程的下拉框代理"""
        page_key = 'student_page'
        # 第一次进入该页面，初始化数据模型
        if page_key not in self.initialized_pages:
            self.initialized_pages.add(page_key)
            # 初始化学生数据模型
            self.student_dao = StudentDAO(self.db)
            self.student_table_model = StudentTableModel(self.student_dao)
            self.table_view_students.setModel(self.student_table_model) 
            self.table_view_students.setSelectionBehavior(QAbstractItemView.SelectRows) 
            self.btn_add_stu.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(self.page_map['enter_stu_page']))
            self.btn_delete_stu.clicked.connect(self.on_delete_stu_clicked)
            self.btn_add_stu_without_face.clicked.connect(self.on_add_stu_without_face_clicked)

            # 设置下拉框代理
            self.course_combo_delegate = MyComboDelegate(self.table_view_students)
            self.table_view_students.setItemDelegateForColumn(5, self.course_combo_delegate)
            for row in range(self.student_table_model.rowCount()):
                self.table_view_students.openPersistentEditor(
                    self.student_table_model.index(row, 5)
                )
            # 设置管理课程代理
            self.manage_course_delegate = BtnDelegate('管理课程', self.table_view_students)
            self.manage_course_delegate.btn_clicked_signal.connect(self.on_manage_course_clicked)
            self.table_view_students.setItemDelegateForColumn(6, self.manage_course_delegate)
            for row in range(self.student_table_model.rowCount()):
                self.table_view_students.openPersistentEditor(
                    self.student_table_model.index(row, 6)
                )

            # 设置管理人脸录入代理
            self.manage_face_delegate = BtnDelegate('(重新)录入人脸',self.table_view_students)
            self.manage_face_delegate.btn_clicked_signal.connect(self.on_manage_face_clicked)   
            self.table_view_students.setItemDelegateForColumn(7, self.manage_face_delegate)
            for row in range(self.student_table_model.rowCount()):
                self.table_view_students.openPersistentEditor(
                    self.student_table_model.index(row, 7)
            )


        elif self.data_dirty[page_key]:
            #如果数据脏了，仅仅刷新数据模型即可
            self.student_table_model.refresh()
            self.reset_delegates()

        self.data_dirty[page_key] = False  # 刷新后当前页面不是脏的
        self.stacked_widget.setCurrentIndex(self.page_map['student_page'])

    def on_delete_stu_clicked(self):
        """删除学生信息"""
        selected_indexes = self.table_view_students.selectionModel().selectedRows()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            self.student_dao.delete_student(selected_row)
            # 刷新学生数据模型以及对应的课程数据模型
            self.student_table_model.refresh()
            self.reset_delegates()

    def on_add_stu_without_face_clicked(self):
        """添加简单的学生信息，不带有人脸的"""
        input_dialog = StudentInputDialog()
        if input_dialog.exec() == QDialog.Accepted:
            res = input_dialog.get_value()
            if len(res) == 0:
                print('请输入正确的课程信息')
                return
            name = res['name']
            gender = res['gender']
            age = res['age']
            self.student_dao.add_student(name, gender, age, 0)
            
            self.student_table_model.refresh()
            self.reset_delegates()
        
    def on_manage_face_clicked(self, row):
        """对学生的人脸进行管理， 进入人脸管理页面，并且重新录入人脸"""
        pass

    def on_manage_course_clicked(self, row):
        """管理学生的课程，包括课程的增删,
        这里没有设置该页面是否为脏页面的原因是，一个学生的课程数量不过就几门最多十几门，因此没必要使用懒加载"""
        self.stu_course_dao = StuCourseDao(self.db)
        self.stu_course_model = CourseStuModel(self.stu_course_dao, self.student_table_model.data_cache[row][0])    
        self.table_view_stu_course.setModel(self.stu_course_model)
        self.table_view_stu_course.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view_stu_course.setSelectionMode(QAbstractItemView.ExtendedSelection)     
                
        self.stu_course_available_model = CourseStuAvailableModel(self.stu_course_dao, self.student_table_model.data_cache[row][0])
        self.table_view_stu_course_availabel.setModel(self.stu_course_available_model)
        self.table_view_stu_course_availabel.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view_stu_course_availabel.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.stacked_widget.setCurrentIndex(self.page_map['stu_course_page'])


        # 给添加和移除按钮连接槽函数
        self.btn_add_course_for_stu.clicked.connect(lambda: self.on_add_stu_to_course(row))
        self.btn_del_course_for_stu.clicked.connect(lambda: self.on_del_course_for_stu(row))



    def on_add_stu_to_course(self, row):
        """选择还能选的课程，一次性添加到学生的选课表中"""
        selected_indexes = self.table_view_stu_course_availabel.selectionModel().selectedRows()
        if selected_indexes:
            course_names = [self.stu_course_available_model.data(index, Qt.DisplayRole) for index in selected_indexes]
            stu_id = self.student_table_model.data_cache[row][0]
            self.stu_course_dao.add_stu_to_courses(stu_id, course_names)
            self.stu_course_model.refresh()
            self.stu_course_available_model.refresh()
            
            self.set_page_dirty(['student_page'])

    def on_del_course_for_stu(self, row):
        """删除学生的课程"""
        selected_indexes = self.table_view_stu_course.selectionModel().selectedRows()
        if selected_indexes:
            course_names = [self.stu_course_model.data(index, Qt.DisplayRole) for index in selected_indexes]
            stu_id = self.student_table_model.data_cache[row][0]
            self.stu_course_dao.del_course_from_stu(stu_id, course_names)
            self.stu_course_model.refresh()
            self.stu_course_available_model.refresh()

            self.set_page_dirty(['student_page'])


    def reset_delegates(self):
        """重置代理，避免内容不刷新"""
        self.table_view_students.clearSelection()

        for row in range(self.student_table_model.rowCount() + 10):
            try:
                self.table_view_students.closePersistentEditor(self.student_table_model.index(row, 5))
            except:
                pass

        self.table_view_students.setItemDelegateForColumn(5, None)
        self.course_combo_delegate.deleteLater()

        QApplication.processEvents()  # 处理事件，确保UI更新

        self.course_combo_delegate = MyComboDelegate(self.table_view_students)
        self.table_view_students.setItemDelegateForColumn(5, self.course_combo_delegate)

        for row in range(self.student_table_model.rowCount()):
            self.table_view_students.openPersistentEditor(
                self.student_table_model.index(row, 5)
            )



#-------------------------------页面切换相关代码------------------------------------------------------------
    def set_page_dirty(self, page_keys):
        """设置页面为脏，表示需要刷新数据"""
        for page_key in page_keys:
            self.data_dirty[page_key] = True
    
    def on_tree_widget_clicked(self, item, column):
        """管理页面的切换，点击不同的导航栏进入不同的页面"""
        item_name = item.text(column)

        # 显示一个小的加载指示器
        self.status_bar.showMessage(f'正在加载 {item_name}...')
        QApplication.processEvents()  # 处理事件，确保UI更新

        if item_name == '老师管理':
            self.enter_page_teacher()
        elif item_name == '课程管理':
            self.enter_page_course()
        elif item_name == '学生管理':
            self.enter_page_student()
        elif item_name == '退出':
            from src.ui.login_window import LoginWindow
            self.login_window = LoginWindow(self.db)
            self.login_window.show()
            self.close()
        elif item_name == '返回':
            if self.stacked_widget.currentIndex() == 0:
                pass
            else:
                cur_index = self.stacked_widget.currentIndex()
                self.stacked_widget.setCurrentIndex(cur_index - 1)
        else: 
            pass

        self.status_bar.showMessage('加载完成', 2000)

# --------------------人脸录入相关代码------------------------------------------------------------

    def delayed_model_init(self):
        """在qt界面完全创建后再进行模型的初始化，避免系统崩溃"""
        self.preload_thread = ModelPreloadThread()
        self.preload_thread.preload_finished.connect(self.on_model_preloaded)
        self.preload_thread.start()
        self.status_bar.showMessage('正在加载模型...')

        #暂时禁用按钮
        self.btn_start_enter.setEnabled(False)
        self.btn_start_enter.setText('正在加载模型...')

    def on_model_preloaded(self, models):
        """模型预加载完成的回调"""
        self.preloaded_models = models
        self.status_bar.showMessage('模型加载完成')
        self.btn_start_enter.setEnabled(True)
        self.btn_start_enter.setText('开始录入')


    def start_enter_stu_with_face(self):
        """ 下面是关于人脸录入的相关函数，为了避免与界面管理的代码混在一起，因此单独将其
        放到下边，使用注释进行分割
        """        
        if self.face_taker is not None:
            return
        
        #显示加载进度指示
        self.setCursor(Qt.WaitCursor)

        # face_taker创建
        self.face_taker = FaceTaker(my_config.VIDEO_PATH, self.preloaded_models)
        self.face_taker.update_frame_signal.connect(self.update_frame)
        self.face_taker.select_face_signal.connect(self.get_face)

        self.btn_confirm_collect.clicked.connect(self.confirm_face_take)
        self.btn_pass_collect.clicked.connect(self.face_taker.resume)

        # 添加状态指示
        self.status_bar.showMessage('正在启动摄像头...')

        # 使用非阻塞方式启动
        QTimer.singleShot(100, self.delayed_start_face_taker)

    def delayed_start_face_taker(self):
        """延迟启动线程，避免UI阻塞"""
        self.face_taker.start()
        self.status_bar.showMessage('正在录入人脸...')
        self.setCursor(Qt.ArrowCursor)

    def confirm_face_take(self):
        if self.cur_face is None:
            return
        face_feature = self.face_taker.get_face_feature()

        name = self.line_edit_name.text()
        age = self.line_edit_age.text()
        if self.rbtn_male.isChecked():
            gender = '男'
        elif self.rbtn_female.isChecked():
            gender = '女'
        else:
            gender = ''

        if name == ' ' or age == '  ' or gender == '':
            print('请输入正确的人脸信息')
            return
        
        is_face_collected = 1
        self.student_dao.add_student(name, gender, age, is_face_collected, face_feature)
        self.student_table_model.refresh()
        self.face_taker.resume()

        self.cur_face = None

    def update_frame(self, qimage):
        label_size = self.label_camp_frame.size()
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
        self.label_camp_frame.setPixmap(pixmap)

    def get_face(self, qimage):
        self.cur_face = qimage
        pixmap = QPixmap.fromImage(qimage)
        self.label_face.setPixmap(pixmap)

    def end_enter_face(self):
        if self.face_taker is not None:
            self.face_taker.stop()
            self.face_taker = None
            self.student_dao.save_vec_db()
            self.stacked_widget.setCurrentIndex(3)


    def closeEvent(self, event):
        if self.face_taker is not None:
            self.face_taker.stop()
            self.face_taker = None
            self.student_dao.save_vec_db()

        return super().closeEvent(event)


#-------------------------------对话框相关代码------------------------------------------------------------

class StudentInputDialog(QDialog):
    """学生信息输入对话框"""
    def __init__(self):
        super().__init__()
        self.value = {}
        self.setWindowTitle('输入学生信息')
        layout = QFormLayout()

        # 学生姓名输入
        self.name = QLineEdit(self)
        
        # 年龄输入
        self.age = QLineEdit(self)
        
        # 性别选择 - 单选框
        gender_layout = QHBoxLayout()
        self.rbtn_male = QPushButton('男')
        self.rbtn_male.setCheckable(True)
        self.rbtn_female = QPushButton('女')
        self.rbtn_female.setCheckable(True)
        
        # 单选按钮互斥
        self.rbtn_male.clicked.connect(lambda: self.rbtn_female.setChecked(False))
        self.rbtn_female.clicked.connect(lambda: self.rbtn_male.setChecked(False))
        
        gender_layout.addWidget(self.rbtn_male)
        gender_layout.addWidget(self.rbtn_female)

        # 按钮
        self.submit = QPushButton('提交')
        self.submit.clicked.connect(self.accept)

        self.cancel = QPushButton('取消')
        self.cancel.clicked.connect(self.reject)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.submit)
        btn_layout.addWidget(self.cancel)

        # 添加到表单
        layout.addRow('姓名:', self.name)
        layout.addRow('年龄:', self.age)
        layout.addRow('性别:', gender_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def accept(self):
        name = self.name.text()
        age = self.age.text()
        gender = '男' if self.rbtn_male.isChecked() else '女' if self.rbtn_female.isChecked() else ''
        
        if name and age and gender:
            self.value['name'] = name
            self.value['age'] = age
            self.value['gender'] = gender
            super().accept()
        else:
            print('请输入完整的学生信息')

    def reject(self):
        super().reject()

    def get_value(self):
        return self.value

class TeacherInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.value = {}
        self.setWindowTitle('输入老师信息')
        layout = QFormLayout()

        self.name = QLineEdit(self)
        self.username = QLineEdit(self)
        self.pswd = QLineEdit(self)
        self.pswd.setEchoMode(QLineEdit.Password)

        self.submit = QPushButton('提交')
        self.submit.clicked.connect(self.accept)

        self.cancel = QPushButton('取消')
        self.cancel.clicked.connect(self.reject)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.submit)
        btn_layout.addWidget(self.cancel)

        layout.addRow('姓名:', self.name)
        layout.addRow('用户名', self.username)
        layout.addRow('密码', self.pswd)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)


    def accept(self):
        name = self.name.text()
        username = self.username.text()
        pswd = self.pswd.text()
        if name != '' and username != '' and pswd != '':
            self.value['name'] = name
            self.value['username'] = username
            self.value['pswd'] = pswd
        super().accept()

    def reject(self):
        super().reject()

    def get_value(self):
        return self.value

class CourseInputDialog(QDialog):
    def __init__(self, teacher_dao: TeacherDAO):
        super().__init__()
        self.value = {}
        self.setWindowTitle('输入课程信息')
        layout = QFormLayout()

        self.course_name = QLineEdit(self)
        self.teacher_username = QComboBox(self)
        res = teacher_dao.get_data()
        for teacher_info in res:
            self.teacher_username.addItem(teacher_info[1])

        self.submit = QPushButton('提交')
        self.submit.clicked.connect(self.accept)

        self.cancel = QPushButton('取消')
        self.cancel.clicked.connect(self.reject)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.submit)
        btn_layout.addWidget(self.cancel)

        layout.addRow('课程名:', self.course_name)
        layout.addRow('所属老师', self.teacher_username)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)


    def accept(self):
        course_name = self.course_name.text()
        teacher_username = self.teacher_username.currentText()
        if course_name != '' and teacher_username != '':
            self.value['course_name'] = course_name
            self.value['teacher_username'] = teacher_username
        super().accept()

    def reject(self):
        super().reject()

    def get_value(self):
        return self.value
