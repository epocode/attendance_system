import os
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
    QApplication,
    QLabel,
    QMessageBox
)
from PySide6.QtCore import Signal, QTimer, Qt, QSize, QSortFilterProxyModel
from PySide6.QtGui import QPixmap, QPainter, QImage
import cv2
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

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AdminWindow(Ui_AdminWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tree_widget.setCurrentItem(self.tree_widget.topLevelItem(1))
        #当前窗口要维护的信息
        self.db = DataBase()
        self.page_map = {"teacher_page":0, "course_page": 1,
                         "student_page":2, "stu_course_page":3,
                         "enter_stu_page": 5, "enter_multi_stu_page": 4}
        self.page_map_to_navi_info = {
            "teacher_page": "老师管理",
            "course_page": "课程管理",
            "student_page": "学生管理",
            "stu_course_page": "学生管理>学生课程管理",
            "enter_stu_page": "学生管理>重新录入学生人脸",
            "enter_multi_stu_page": "学生管理>批量录入学生信息",
        }
        
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
        self.show_navi_info_label = QLabel()
        self.status_bar.addPermanentWidget(self.show_navi_info_label)
        self.show_navi_info_label.setText(self.page_map_to_navi_info['teacher_page'])

        # 初始化视频来源下拉框的内容。
        self.setup_source_combo_box()

    
    #选择视频来源
    def setup_source_combo_box(self):
        # 设置批量录入界面的视频来源下拉框
        self.combo_box_video_source.addItem("摄像头", 0)
        self.combo_box_video_source.addItem("视频文件", 'video_file')
        my_config.VIDEO_PATH = 0
        self.combo_box_video_source.currentIndexChanged.connect(self.on_source_selection_changed)

        # 设置重新录入界面的视频来源下拉框
        self.combo_box_select_video_source.addItem("摄像头", 0)
        self.combo_box_select_video_source.addItem("视频文件", 'video_file')
        my_config.VIDEO_PATH = 0
        self.combo_box_select_video_source.currentIndexChanged.connect(self.on_source_selection_changed)

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

            # Create and set up the filter input and proxy model only once
            self.teacher_proxy_model = QSortFilterProxyModel(self)
            self.teacher_proxy_model.setSourceModel(self.teacher_table_model)
            self.teacher_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive) # Set once
            self.teacher_proxy_model.setFilterKeyColumn(-1) # Filter on all columns by default

            self.table_view_teachers.setModel(self.teacher_proxy_model)
            self.table_view_teachers.setSortingEnabled(True)

            # Create filter QLineEdit
            self.teacher_filter_input = QLineEdit(self)
            self.teacher_filter_input.setPlaceholderText("输入关键字筛选老师...")
            self.teacher_filter_input.textChanged.connect(self.filter_teachers_table)

            # Add QLineEdit to the layout of page_teacher
            # Assuming self.page_teacher is self.stacked_widget.widget(0)
            page_teacher_widget = self.stacked_widget.widget(0) 
            if page_teacher_widget.layout() is None:
                # If no layout exists, create a new QVBoxLayout
                new_layout = QVBoxLayout(page_teacher_widget)
                page_teacher_widget.setLayout(new_layout)
            
            # Insert the filter input at the top of the layout
            # This might need adjustment based on the actual structure of ui_admin_window.py
            # It assumes other widgets (like buttons) are potentially in a different part of the UI
            # or this layout is the primary one for the table and its controls.
            # A more robust way might be to ensure specific layout objects exist in your .ui file.
            # For now, we'll try to insert into the existing layout or a new one.
            
            # Let's find the existing layout that contains the table_view_teachers
            # Typically, the table view and buttons are within a main vertical layout for the page.
            # We assume self.page_teacher's layout is QVBoxLayout.
            # The ui file shows page_teacher has a QVBoxLayout (verticalLayout_4)
            # which contains another QVBoxLayout (verticalLayout) for buttons and the table view.
            # We should insert the filter input into this inner verticalLayout, above the table view.
            
            # Accessing via object names from Ui_AdminWindow setup
            # self.verticalLayout is the layout containing buttons and table_view_teachers
            if hasattr(self, 'verticalLayout') and isinstance(self.verticalLayout, QVBoxLayout):
                 # Insert QLineEdit at the top of this specific layout
                self.verticalLayout.insertWidget(0, self.teacher_filter_input)
            else:
                # Fallback if the specific layout name isn't found (e.g. if UI structure changes)
                # This is less ideal as it might not place the filter correctly.
                current_layout = page_teacher_widget.layout()
                if current_layout is not None:
                    current_layout.insertWidget(0, self.teacher_filter_input)
                else: # Should have been created above if it was None
                    logger.warning("Could not find a suitable layout to insert teacher filter input.")


        # The table should now update automatically via model signals.
        # No need for data_dirty flag for teacher_page.
        self.stacked_widget.setCurrentIndex(self.page_map['teacher_page'])
        self.show_navi_info_label.setText(self.page_map_to_navi_info['teacher_page'])

    def filter_teachers_table(self, text):
        if hasattr(self, 'teacher_proxy_model'):
            self.teacher_proxy_model.setFilterFixedString(text)

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

            self.btn_add_teacher.setEnabled(False)
            self.btn_delete_teacher.setEnabled(False)
            self.status_bar.showMessage("正在添加新老师...")
            QApplication.processEvents() # Ensure message is shown

            try:
                if not self.teacher_dao.check_single_username(username):
                    self.status_bar.showMessage("添加老师失败，用户名已存在。", 3000)
                    # QMessageBox.warning(self, "添加失败", "用户名已存在。") # Alternative
                    return # Keep buttons disabled until dialog is closed or input changes
            
                if self.teacher_table_model.add_teacher(name, username, pswd):
                    self.status_bar.showMessage(f"老师 {name} 添加成功。", 3000)
                else:
                    self.status_bar.showMessage("添加老师失败，发生未知错误。", 3000)
                    # QMessageBox.warning(self, "添加失败", "添加新老师失败。") # Alternative
            finally:
                self.btn_add_teacher.setEnabled(True)
                self.btn_delete_teacher.setEnabled(True)
        
    def on_delete_teacher_clicked(self):
        selected_indexes = self.table_view_teachers.selectionModel().selectedRows()
        if not selected_indexes:
            self.status_bar.showMessage("请先选择要删除的老师。", 2000)
            return

        # Get the proxy model index for the selected row
        proxy_model_index = selected_indexes[0]
        # Map to the source model index
        source_model_index = self.teacher_proxy_model.mapToSource(proxy_model_index)
        source_row = source_model_index.row()

        # Get teacher name from the source model for the confirmation dialog
        # Assuming column 0 is '姓名' (Name)
        teacher_name_to_delete = self.teacher_table_model.data(self.teacher_table_model.index(source_row, 0), Qt.DisplayRole)
        # Fallback if name is not found, though it should be
        if teacher_name_to_delete is None:
            teacher_name_to_delete = "所选老师"


        reply = QMessageBox.question(self, '确认删除', 
                                     f"确定要删除老师 “{teacher_name_to_delete}” 吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.btn_add_teacher.setEnabled(False)
            self.btn_delete_teacher.setEnabled(False)
            self.status_bar.showMessage(f"正在删除老师 {teacher_name_to_delete}...")
            QApplication.processEvents() # Ensure message is shown

            try:
                # Call delete_teacher_by_index with the source model's row index
                if self.teacher_table_model.delete_teacher_by_index(source_row):
                    self.status_bar.showMessage(f"老师 {teacher_name_to_delete} 已删除。", 3000)
                else:
                    self.status_bar.showMessage("删除老师失败。", 3000)
                    # QMessageBox.warning(self, "删除失败", "删除老师失败。") # Alternative
            finally:
                self.btn_add_teacher.setEnabled(True)
                self.btn_delete_teacher.setEnabled(True)

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

        # The table should now update automatically via model signals.
        # No need for data_dirty flag for course_page.
        self.stacked_widget.setCurrentIndex(self.page_map['course_page'])
        self.show_navi_info_label.setText(self.page_map_to_navi_info['course_page'])

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

            self.btn_add_course.setEnabled(False)
            self.btn_delete_course.setEnabled(False)
            self.status_bar.showMessage("正在添加新课程...")
            QApplication.processEvents()

            try:
                if not self.course_dao.check_single_course_name(course_name):
                    self.status_bar.showMessage("添加课程失败，课程名已存在。", 3000)
                    # QMessageBox.warning(self, "添加失败", "课程名已存在。")
                    return # Keep buttons disabled until dialog is closed or input changes
            
                if self.course_table_model.add_course(course_name, teacher_username):
                    self.status_bar.showMessage(f"课程 {course_name} 添加成功。", 3000)
                else:
                    self.status_bar.showMessage("添加课程失败，发生未知错误。", 3000)
                    # QMessageBox.warning(self, "添加失败", f"添加课程 {course_name} 失败。")
            finally:
                self.btn_add_course.setEnabled(True)
                self.btn_delete_course.setEnabled(True)
        
    def on_delete_course_clicked(self):
        selected_indexes = self.table_view_course.selectionModel().selectedRows()
        if not selected_indexes:
            self.status_bar.showMessage("请先选择要删除的课程。", 2000)
            return

        selected_row = selected_indexes[0].row()
        course_name_to_delete = self.course_table_model.data_cache[selected_row][0]

        reply = QMessageBox.question(self, '确认删除', 
                                     f"确定要删除课程 “{course_name_to_delete}” 吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.btn_add_course.setEnabled(False)
            self.btn_delete_course.setEnabled(False)
            self.status_bar.showMessage(f"正在删除课程 {course_name_to_delete}...")
            QApplication.processEvents()

            try:
                if self.course_table_model.delete_course_by_index(selected_row):
                    self.status_bar.showMessage(f"课程 {course_name_to_delete} 已删除。", 3000)
                else:
                    self.status_bar.showMessage("删除课程失败。", 3000)
                    # QMessageBox.warning(self, "删除失败", "删除课程失败。")
            finally:
                self.btn_add_course.setEnabled(True)
                self.btn_delete_course.setEnabled(True)



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
            self.btn_add_stu.clicked.connect(self.on_add_multi_stu_clicked)
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


        # The table should now update automatically via model signals for add/delete.
        # No need for data_dirty flag for student_page.
        # However, reset_delegates might still be needed after model operations
        # if not called directly in on_delete_stu_clicked or on_add_stu_without_face_clicked.
        # For now, we assume add/delete handlers will call reset_delegates if needed.
        self.stacked_widget.setCurrentIndex(self.page_map['student_page'])
        self.show_navi_info_label.setText(self.page_map_to_navi_info['student_page'])

    def on_delete_stu_clicked(self):
        """删除学生信息"""
        selected_indexes = self.table_view_students.selectionModel().selectedRows()
        if not selected_indexes:
            self.status_bar.showMessage("请先选择要删除的学生。", 2000)
            return

        selected_row = selected_indexes[0].row()
        student_name_to_delete = self.student_table_model.data_cache[selected_row][1] # Name is at index 1

        reply = QMessageBox.question(self, '确认删除', 
                                     f"确定要删除学生 “{student_name_to_delete}” 吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.btn_add_stu.setEnabled(False)
            self.btn_delete_stu.setEnabled(False)
            self.btn_add_stu_without_face.setEnabled(False)
            self.status_bar.showMessage(f"正在删除学生 {student_name_to_delete}...")
            QApplication.processEvents()

            try:
                if self.student_table_model.delete_student_by_index(selected_row):
                    self.status_bar.showMessage(f"学生 {student_name_to_delete} 已删除。", 3000)
                    self.reset_delegates() # Keep for UI consistency
                else:
                    self.status_bar.showMessage("删除学生失败。", 3000)
                    # QMessageBox.warning(self, "删除失败", "删除学生信息失败。")
            finally:
                self.btn_add_stu.setEnabled(True)
                self.btn_delete_stu.setEnabled(True)
                self.btn_add_stu_without_face.setEnabled(True)


    def on_add_stu_without_face_clicked(self):
        """添加简单的学生信息，不带有人脸的"""
        input_dialog = StudentInputDialog()
        if input_dialog.exec() == QDialog.Accepted:
            res = input_dialog.get_value()
            if len(res) == 0:
                # User likely closed dialog without submitting valid data
                return 
            name = res['name']
            gender = res['gender']
            age = res['age']

            self.btn_add_stu.setEnabled(False)
            self.btn_delete_stu.setEnabled(False)
            self.btn_add_stu_without_face.setEnabled(False)
            self.status_bar.showMessage(f"正在添加学生 {name}...")
            QApplication.processEvents()

            try:
                if self.student_table_model.add_student_data(name, gender, age, is_face_collected=0, face_feature=None):
                    self.status_bar.showMessage(f"学生 {name} 添加成功。", 3000)
                    self.reset_delegates() # Keep for UI consistency
                else:
                    self.status_bar.showMessage("添加学生失败，发生未知错误。", 3000)
                    # QMessageBox.warning(self, "添加失败", "添加学生信息失败。")
            finally:
                self.btn_add_stu.setEnabled(True)
                self.btn_delete_stu.setEnabled(True)
                self.btn_add_stu_without_face.setEnabled(True)
    
    def on_add_multi_stu_clicked(self):
        """"批量添加学生信息"""
        self.btn_start_enter.clicked.connect(self.start_enter_stu_with_face)
        self.btn_end_enter.clicked.connect(self.end_enter_face)
        self.btn_confirm_collect.clicked.connect(self.confirm_face_take)

        self.stacked_widget.setCurrentIndex(self.page_map['enter_multi_stu_page'])
        self.show_navi_info_label.setText(self.page_map_to_navi_info['enter_multi_stu_page'])
        

    def on_manage_face_clicked(self, row):
        """对学生的人脸进行管理， 进入人脸管理页面，并且重新录入人脸.
        这里没必要使用懒加载。
        使用row得到学生的ID，从而得到姓名、性别、年龄等信息"""
        id_index =  self.student_table_model.index(row, 0)
        name_index =self.student_table_model.index(row, 1)
        gender_index = self.student_table_model.index(row, 2)
        age_index = self.student_table_model.index(row, 3)

        id = self.student_table_model.data(id_index, Qt.DisplayRole)
        name = self.student_table_model.data(name_index, Qt.DisplayRole)
        gender = self.student_table_model.data(gender_index, Qt.DisplayRole)
        age = self.student_table_model.data(age_index, Qt.DisplayRole)

        # 显示学生信息
        self.label_id_1.setText(str(id))
        self.label_name_1.setText(name)
        self.label_gender_1.setText(gender)
        self.label_age_1.setText(str(age))

        # 先断开所有连接
        try:
            if self.btn_start_cap_face_1.receivers(self.btn_start_cap_face_1.clicked) > 0:
                self.btn_start_cap_face_1.clicked.disconnect()
            if self.btn_end_cap_face_1.receivers(self.btn_end_cap_face_1.clicked) > 0:
                self.btn_end_cap_face_1.clicked.disconnect()
            if self.btn_confirm_this_face_1.receivers(self.btn_confirm_this_face_1.clicked) > 0:
                self.btn_confirm_this_face_1.clicked.disconnect()  
        except TypeError:
            pass
        self.btn_start_cap_face_1.clicked.connect(self.start_re_enter_face)
        self.btn_end_cap_face_1.clicked.connect(self.end_face_take_1)
        self.btn_confirm_this_face_1.clicked.connect(self.confirm_face_take_1)

        self.face_taker = None
        self.cur_face = None


        self.stacked_widget.setCurrentIndex(self.page_map['enter_stu_page'])
        self.show_navi_info_label.setText(self.page_map_to_navi_info['enter_stu_page'])

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
        self.show_navi_info_label.setText(self.page_map_to_navi_info['stu_course_page'])


        # 给添加和移除按钮连接槽函数
        self.btn_add_course_for_stu.clicked.connect(lambda: self.on_add_stu_to_course(row))
        self.btn_del_course_for_stu.clicked.connect(lambda: self.on_del_course_for_stu(row))



    def on_add_stu_to_course(self, row):
        """选择还能选的课程，一次性添加到学生的选课表中"""
        selected_indexes = self.table_view_stu_course_availabel.selectionModel().selectedRows()
        if selected_indexes:
            self.btn_add_course_for_stu.setEnabled(False)
            self.btn_del_course_for_stu.setEnabled(False)
            self.status_bar.showMessage("正在为学生添加课程...")
            QApplication.processEvents() # Ensure message is shown

            try:
                course_names = [self.stu_course_available_model.data(index, Qt.DisplayRole) for index in selected_indexes]
                stu_id = self.student_table_model.data_cache[row][0] # 'row' here is the student's row in student_table_model
                
                self.stu_course_dao.add_stu_to_courses(stu_id, course_names) 
                
                self.stu_course_model.refresh() 
                self.stu_course_available_model.refresh()
                self.status_bar.showMessage("课程添加成功。", 3000)
            except Exception as e:
                self.status_bar.showMessage(f"添加课程失败: {e}", 5000) # Show error for longer
                logger.error(f"Error in on_add_stu_to_course: {e}")
            finally:
                self.btn_add_course_for_stu.setEnabled(True)
                self.btn_del_course_for_stu.setEnabled(True)
        else:
            self.status_bar.showMessage("请先选择要添加的课程。", 2000)


    def on_del_course_for_stu(self, row):
        """删除学生的课程"""
        selected_indexes = self.table_view_stu_course.selectionModel().selectedRows()
        if selected_indexes:
            course_names_to_delete = [self.stu_course_model.data(index, Qt.DisplayRole) for index in selected_indexes]
            # 'row' is the student's row in the main student_table_model, used to get student's name for the message
            student_name = self.student_table_model.data_cache[row][1] 

            reply = QMessageBox.question(self, '确认移除课程', 
                                         f"确定要为学生 “{student_name}” 移除选中的 {len(course_names_to_delete)} 门课程吗？",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.btn_add_course_for_stu.setEnabled(False)
                self.btn_del_course_for_stu.setEnabled(False)
                self.status_bar.showMessage(f"正在为学生 {student_name} 移除课程...")
                QApplication.processEvents() # Ensure message is shown

                try:
                    stu_id = self.student_table_model.data_cache[row][0]
                    self.stu_course_dao.del_course_from_stu(stu_id, course_names_to_delete)
                    
                    self.stu_course_model.refresh()
                    self.stu_course_available_model.refresh()
                    self.status_bar.showMessage("课程移除成功。", 3000)
                except Exception as e:
                    self.status_bar.showMessage(f"移除课程失败: {e}", 5000) # Show error for longer
                    logger.error(f"Error in on_del_course_for_stu: {e}")
                finally:
                    self.btn_add_course_for_stu.setEnabled(True)
                    self.btn_del_course_for_stu.setEnabled(True)
        else:
            self.status_bar.showMessage("请先选择要移除的课程。", 2000)


    def reset_delegates(self):
        """重置代理，避免内容不刷新"""
        self.table_view_students.clearSelection()

        for row in range(self.student_table_model.rowCount() + 10):
            try:
                self.table_view_students.closePersistentEditor(self.student_table_model.index(row, 5))
                self.table_view_students.closePersistentEditor(self.student_table_model.index(row, 6))
                self.table_view_students.closePersistentEditor(self.student_table_model.index(row, 7))
            except:
                pass

        self.table_view_students.setItemDelegateForColumn(5, None)
        self.table_view_students.setItemDelegateForColumn(6, None)
        self.table_view_students.setItemDelegateForColumn(7, None)

        self.course_combo_delegate.deleteLater()
        self.manage_course_delegate.deleteLater()
        self.manage_face_delegate.deleteLater()




        QApplication.processEvents()  # 处理事件，确保UI更新

        self.course_combo_delegate = MyComboDelegate(self.table_view_students)
        self.table_view_students.setItemDelegateForColumn(5, self.course_combo_delegate)
        self.manage_course_delegate = BtnDelegate('管理课程', self.table_view_students)
        self.manage_course_delegate.btn_clicked_signal.connect(self.on_manage_course_clicked)
        self.table_view_students.setItemDelegateForColumn(6, self.manage_course_delegate)
        self.manage_face_delegate = BtnDelegate('(重新)录入人脸',self.table_view_students)
        self.manage_face_delegate.btn_clicked_signal.connect(self.on_manage_face_clicked)
        self.table_view_students.setItemDelegateForColumn(7, self.manage_face_delegate)


        for row in range(self.student_table_model.rowCount()):
            self.table_view_students.openPersistentEditor(
                self.student_table_model.index(row, 5)
            )
            self.table_view_students.openPersistentEditor(
                self.student_table_model.index(row, 6)
            )
            self.table_view_students.openPersistentEditor(
                self.student_table_model.index(row, 7)  
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
        # QApplication.processEvents()  # Removed: To see if UI updates promptly without it.

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
            cur_page_idx = self.stacked_widget.currentIndex()
            if cur_page_idx == self.page_map['stu_course_page'] or cur_page_idx == self.page_map['enter_stu_page'] or cur_page_idx == self.page_map['enter_multi_stu_page']:
                self.enter_page_student()
            else:
                pass    
        else: 
            pass

        self.status_bar.showMessage('页面加载完成', 1)

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
    
        #显示加载进度指示
        self.setCursor(Qt.WaitCursor)

        # 断开之前所有的连接
        try:
            self.btn_pass_collect.clicked.disconnect()
        except TypeError:
            pass

        # face_taker创建
        self.face_taker = FaceTaker(my_config.VIDEO_PATH, self.preloaded_models)
        self.face_taker.update_frame_signal.connect(self.update_frame)
        self.face_taker.select_face_signal.connect(self.get_face)
        
        
        self.btn_pass_collect.clicked.connect(self.face_taker.resume)
        # 添加状态指示
        self.status_bar.showMessage('正在启动摄像头...')

        # 使用非阻塞方式启动
        # Pass context for different status messages
        QTimer.singleShot(100, lambda: self.delayed_start_face_taker(is_bulk_entry=True))

    def delayed_start_face_taker(self, is_bulk_entry=True):
        """延迟启动线程，避免UI阻塞"""
        self.face_taker.start()
        if is_bulk_entry:
            self.status_bar.showMessage("摄像头已启动，请将人脸对准摄像头。")
        else: # For single re-entry
            self.status_bar.showMessage("摄像头已启动，请将人脸对准摄像头进行重新录入。")
        self.setCursor(Qt.ArrowCursor)

    

    def update_frame(self, qimage):
        label_size = QSize(640, 480)
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
        
        # Get the size of the label
        label_size = QSize(150, 150)
        
        # Convert QImage to QPixmap
        img_pixmap = QPixmap.fromImage(qimage)
        
        # Scale the image proportionally to fit within the label
        scaled_pixmap = img_pixmap.scaled(
            label_size,
            Qt.KeepAspectRatio,  # Maintain aspect ratio
            Qt.SmoothTransformation  # Use smooth scaling algorithm
        )
        
        # Set the scaled pixmap to the label
        self.label_face.setPixmap(scaled_pixmap)
        self.status_bar.showMessage("检测到人脸，请输入学生信息并确认。", 3000)


    def confirm_face_take(self):
        if self.cur_face is None:
            QMessageBox.warning(self, "无选中人脸", "请先确保已通过摄像头捕捉到人脸。")
            return
            
        name = self.line_edit_name.text().strip()
        age = self.line_edit_age.text().strip()
        gender = ''
        if self.rbtn_male.isChecked():
            gender = '男'
        elif self.rbtn_female.isChecked():
            gender = '女'

        if not name or not age or not gender: # Check for empty strings
            QMessageBox.warning(self, "信息不完整", "请输入完整的学生姓名、年龄和性别。")
            return
        
        self.status_bar.showMessage(f"正在保存学生 {name} 的信息及人脸特征...")
        face_feature = self.face_taker.get_face_feature()
        is_face_collected = 1
        
        # Call model's method
        if self.student_table_model.add_student_data(name, gender, age, is_face_collected, face_feature):
            self.status_bar.showMessage(f"学生 {name} 的信息保存成功！请继续下一位或结束录入。", 4000)
            # Clear input fields
            self.line_edit_name.clear()
            self.line_edit_age.clear()
            # Assuming rbtn_male and rbtn_female are part of a QButtonGroup that handles exclusivity,
            # or they need to be manually unchecked. If they are independent, this is fine.
            self.rbtn_male.setChecked(False) 
            self.rbtn_female.setChecked(False)
            self.label_face.clear() # Clear the displayed face
            self.cur_face = None # Reset current face
        else:
            QMessageBox.warning(self, '人脸录入失败', '添加学生数据失败或人脸已存在。')
            self.status_bar.showMessage("保存失败，可能人脸已存在或输入信息有误。", 3000)
        
        self.face_taker.resume() # Allow next face capture
   

    def end_enter_face(self):
        if self.face_taker is not None:
            self.status_bar.showMessage("批量人脸录入已结束。", 3000)
            blank_img = cv2.cvtColor(cv2.imread(os.path.join(my_config.PHOTO_PATH, 'blank.jpg')), cv2.COLOR_BGR2RGB)
            blank_img_s = cv2.cvtColor(cv2.imread(os.path.join(my_config.PHOTO_PATH, 'blank_s.jpg')), cv2.COLOR_BGR2RGB)
            
            h, w, ch = blank_img.shape
            qimage = QImage(blank_img, w, h, w * ch, QImage.Format_RGB888)
            self.update_frame(qimage)
            
            h, w, ch = blank_img_s.shape
            qimage_s = QImage(blank_img_s, w, h, w * ch, QImage.Format_RGB888)
            self.get_face(qimage_s)
            # QApplication.processEvents() # Removed

            self.face_taker.stop()
            self.face_taker = None


    def closeEvent(self, event):
        if hasattr(self, 'face_taker') and self.face_taker is not None:
            self.face_taker.stop()
            self.face_taker = None

        return super().closeEvent(event)


#-------------------------------人脸重新录入相关代码------------------------------------------------------------
    def start_re_enter_face(self):
        """进入重新录入人脸的界面"""
        if self.face_taker is not None:
            return
        self.face_taker = FaceTaker(my_config.VIDEO_PATH, self.preloaded_models)
        self.face_taker.update_frame_signal.connect(self.update_frame_1)
        self.face_taker.select_face_signal.connect(self.get_face_1)

        try:
            if self.btn_pass_this_face_1.receivers(self.btn_pass_this_face_1.clicked) > 0:
                self.btn_pass_this_face_1.clicked.disconnect()
        except TypeError:
            pass
        self.btn_pass_this_face_1.clicked.connect(self.on_pass_this_face_clicked)
        # 添加状态指示
        self.status_bar.showMessage('正在启动摄像头...')

        # 使用非阻塞方式启动
        QTimer.singleShot(100, lambda: self.delayed_start_face_taker(is_bulk_entry=False))

  
    def update_frame_1(self, qimage):
        # 将捕获到的图片显示在label中
        # label_size = self.lable_display_cap_1.size()
        label_size = QSize(640, 480)
        pixmap = QPixmap(label_size)
        pixmap.fill(Qt.black)  # 设置背景色
        img_pixmap = QPixmap.fromImage(qimage)
        scaled_pixmap = img_pixmap.scaled(
            label_size, 
            Qt.KeepAspectRatio,  # 保持宽高比
            Qt.SmoothTransformation  # 使用平滑的缩放算法
        ) 
        painter = QPainter(pixmap)
        x = (label_size.width() - scaled_pixmap.width()) // 2
        y = (label_size.height() - scaled_pixmap.height()) // 2
        
        # 在指定位置绘制缩放后的图像
        painter.drawPixmap(x, y, scaled_pixmap)
        painter.end()

        self.lable_display_cap_1.setPixmap(pixmap)

    
    def get_face_1(self, qimage):
        """将识别到的人脸放在label上"""
        self.cur_face = qimage
        label_size = QSize(150, 150)
        img_pixmap = QPixmap.fromImage(qimage)
        scaled_pixmap = img_pixmap.scaled(
            label_size,
            Qt.KeepAspectRatio,  # Maintain aspect ratio
            Qt.SmoothTransformation  # Use smooth scaling algorithm
        )
        self.label_display_cap_face_1.setPixmap(scaled_pixmap)
        self.status_bar.showMessage("检测到人脸，请确认是否使用此图像。", 3000)

    def confirm_face_take_1(self):
        """确定将这张人脸录入数据库，因为对于重新录入人脸这个过程来说，录上了就可以直接退出了"""
        if self.cur_face is None:
            QMessageBox.warning(self, "无选中人脸", "请先确保已通过摄像头捕捉到人脸。")
            return
        
        student_name_for_status = self.label_name_1.text() # Get name before potential clear
        self.status_bar.showMessage(f"正在为学生 {student_name_for_status} 更新人脸特征...")
        face_feature = self.face_taker.get_face_feature()
        id = int(self.label_id_1.text())
        
        if self.student_dao.reset_face(id, face_feature):
             self.student_table_model.refresh() # To ensure 'is_face_collected' status updates in the table
             self.status_bar.showMessage(f"学生 {student_name_for_status} 的人脸特征更新成功！", 3000)
        else:
            self.status_bar.showMessage(f"学生 {student_name_for_status} 的人脸特征更新失败。", 3000)
            QMessageBox.warning(self, "更新失败", "更新人脸特征失败。")

        # self.set_page_dirty(['student_page']) # Removed
        if self.face_taker: # Ensure face_taker still exists
            self.face_taker.resume() # resume or stop, depending on desired flow
        self.cur_face = None

        # 结束 and clear
        self.end_face_take_1() # This will also set a status message

    def on_pass_this_face_clicked(self):
        """跳过当前人脸录入"""
        if self.face_taker is not None:
            self.face_taker.resume()
            self.status_bar.showMessage("已跳过当前人脸，请对准下一张。", 2000)
        else:
            print("face_taker 不存在")


    def end_face_take_1(self):
        if self.face_taker is not None:
            self.status_bar.showMessage("人脸录入已取消/结束。", 3000)
            blank_img = cv2.cvtColor(cv2.imread(os.path.join(my_config.PHOTO_PATH, 'blank.jpg')), cv2.COLOR_BGR2RGB)
            blank_img_s = cv2.cvtColor(cv2.imread(os.path.join(my_config.PHOTO_PATH, 'blank_s.jpg')), cv2.COLOR_BGR2RGB)
            
            h, w, ch = blank_img.shape
            qimage = QImage(blank_img, w, h, w * ch, QImage.Format_RGB888)
            self.update_frame_1(qimage)
            
            h, w, ch = blank_img_s.shape
            qimage_s = QImage(blank_img_s, w, h, w * ch, QImage.Format_RGB888)
            self.get_face_1(qimage_s)

            # QApplication.processEvents() # Removed
            
            self.face_taker.stop()
            self.face_taker = None
            
        



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
        name = self.name.text().strip()
        age = self.age.text().strip()
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
        name = self.name.text().strip()
        username = self.username.text().strip()
        pswd = self.pswd.text().strip()
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
        course_name = self.course_name.text().strip()
        teacher_username = self.teacher_username.currentText()
        if course_name != '' and teacher_username != '':
            self.value['course_name'] = course_name
            self.value['teacher_username'] = teacher_username
        super().accept()

    def reject(self):
        super().reject()

    def get_value(self):
        return self.value
