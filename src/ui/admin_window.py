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

)
from PySide6.QtCore import Signal, QTimer  
from PySide6.QtGui import QPixmap
from src.ui.ui_files.ui_admin_window import Ui_AdminWindow
from src.db.database import DataBase
from src.db.teacher_dao import TeacherDAO
from src.data_model.teacher_table_model import TeacherTableModel
from src.db.class_dao import ClassDAO
from src.data_model.class_table_model import ClassTableModel
from src.db.student_dao import StudentDAO
from src.data_model.student_table_model import StudentTableModel
from src.core.face_take import FaceTaker
import config.my_config as my_config

class AdminWindow(Ui_AdminWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #当前窗口要维护的信息
        self.db = DataBase()
        
        #老师界面
        self.teacher_dao = TeacherDAO(self.db)
        self.teacher_table_model = TeacherTableModel(self.teacher_dao)
        self.table_view_teachers.setModel(self.teacher_table_model)
        self.table_view_teachers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btn_add_teacher.clicked.connect(self.on_add_teacher_clicked)
        self.btn_delete_teacher.clicked.connect(self.on_delete_teacher_clicked)

        #班级界面
        self.class_dao = ClassDAO(self.db)
        self.class_table_model = ClassTableModel(self.class_dao)
        self.table_view_classes.setModel(self.class_table_model)
        self.table_view_classes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btn_add_class.clicked.connect(self.on_add_class_clicked)
        self.btn_delete_class.clicked.connect(self.on_delete_class_clicked)

        #学生界面
        self.student_dao = StudentDAO(self.db)
        self.student_table_model = StudentTableModel(self.student_dao)
        self.table_view_students.setModel(self.student_table_model) 
        self.table_view_students.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.btn_add_stu.clicked.connect(self.on_add_student_clicked)
        self.btn_delete_stu.clicked.connect(self.on_delete_stu_clicked)
        # QTimer.singleShot(0, self.set_btn_delegate)

        #人脸录入相关
        self.face_taker = None
        self.cur_face = None

        self.btn_start_enter.clicked.connect(self.start_enter_face)
        self.btn_end_enter.clicked.connect(self.end_enter_face)
        
        #绑定功能切换
        self.stacked_widget.setCurrentIndex(0)
        self.tree_widget.itemClicked.connect(self.on_tree_widget_clicked)
        
    # def set_btn_delegate(self):
    #     delegate = ButtonDelegate(self.table_view_students)
    #     delegate.button_clicked_signal.connect(self.on_add_stu_to_class)
    #     self.table_view_students.setItemDelegateForColumn(4, delegate)

    def on_add_stu_to_class(self, row):
        print('加入班级')
    
    def on_delete_stu_clicked(self):
        selected_indexes = self.table_view_students.selectionModel().selectedRows()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            self.student_dao.delete_student(selected_row)
            self.student_table_model.layoutChanged.emit()
    #人脸录入相关函数
    def start_enter_face(self):
        if self.face_taker is not None:
            return
        self.face_taker = FaceTaker(my_config.VIDEO_PATH)
        self.face_taker.update_frame_signal.connect(self.update_frame)
        self.face_taker.select_face_signal.connect(self.get_face)

        self.btn_confirm_collect.clicked.connect(self.confirm_face_take)
        self.btn_pass_collect.clicked.connect(self.face_taker.resume)
        self.face_taker.start()

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
        
        self.student_dao.add_student(face_feature, name, gender, age)
        self.student_table_model.layoutChanged.emit()
        self.face_taker.resume()

        self.cur_face = None

    def update_frame(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
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
            self.teacher_table_model.layoutChanged.emit()
            
    def on_add_student_clicked(self):
        self.stacked_widget.setCurrentIndex(2)

    def on_delete_teacher_clicked(self):
        selected_indexes = self.table_view_teachers.selectionModel().selectedRows()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            self.teacher_dao.delete_row(selected_row)
            self.teacher_table_model.layoutChanged.emit()

    def on_add_class_clicked(self):
        #新增班级
        input_dialog = ClassInputDialog(self.teacher_dao)
        if input_dialog.exec() == QDialog.Accepted:
            res = input_dialog.get_value()
            if len(res) == 0:
                print('请输入正确的班级信息')
                return
            class_name = res['class_name']
            teacher_username = res['teacher_username']
            if not self.class_dao.check_single_class_name(class_name):
                print('当前班级名已经存在')
                return
            self.class_dao.add_new(class_name, teacher_username)
            self.class_table_model.layoutChanged.emit()
        
    def on_delete_class_clicked(self):
        indexes = self.table_view_classes.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            self.class_dao.delete_class_by_row(row)
            self.class_table_model.layoutChanged.emit()
            


    def on_tree_widget_clicked(self, item, column):
        item_name = item.text(column)
        if item_name == '老师管理':
            self.stacked_widget.setCurrentIndex(0)
        elif item_name == '班级管理':
            self.stacked_widget.setCurrentIndex(1)
        elif item_name == '学生管理':
            self.stacked_widget.setCurrentIndex(3)
        elif item_name == '退出':
            from src.ui.login_window import LoginWindow
            self.login_window = LoginWindow(self.db)
            self.login_window.show()
            self.close()
        else: 
            pass

    def closeEvent(self, event):
        if self.face_taker is not None:
            self.face_taker.stop()
            self.face_taker = None
            self.student_dao.save_vec_db()

        return super().closeEvent(event)

class ButtonDelegate(QStyledItemDelegate):
    button_clicked_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = None

    def createEditor(self, parent, option, index):
        if self.button == None:
            self.button = QPushButton('加入班级', parent)
            self.button.setStyleSheet("""
            QPushButton {
                background-color: lightblue;  /* 背景色 */
                color: white;  /* 文字颜色 */
                border-radius: 5px;  /* 圆角 */
                border: 1px solid #007BFF;  /* 边框 */
                padding: 5px 10px;  /* 内边距 */
            }
            QPushButton:hover {
                background-color: #007BFF;  /* 悬停时背景色 */
            }
            QPushButton:pressed {
                background-color: #0056b3;  /* 按下时背景色 */
            }
        """)
            self.button.clicked.connect(lambda:self.button_clicked_signal.emit(index.row()))
            self.button.setGeometry(option.rect)
            self.button.show()
        return self.button
    

        # editor = QWidget(parent)
        # layout = QHBoxLayout(editor)
        # button = QPushButton("加入班级", editor)
        # button.setStyleSheet("""
        #     QPushButton {
        #         background-color: lightblue;  /* 背景色 */
        #         color: white;  /* 文字颜色 */
        #         border-radius: 5px;  /* 圆角 */
        #         border: 1px solid #007BFF;  /* 边框 */
        #         padding: 5px 10px;  /* 内边距 */
        #     }
        #     QPushButton:hover {
        #         background-color: #007BFF;  /* 悬停时背景色 */
        #     }
        #     QPushButton:pressed {
        #         background-color: #0056b3;  /* 按下时背景色 */
        #     }
        # """)
        # layout.addWidget(button)
        # layout.setContentsMargins(0, 0, 0, 0)
        # editor.setLayout(layout)
        # button.clicked.connect(lambda:self.button_clicked_signal.emit(index.row()))
        # return editor
    
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

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

class ClassInputDialog(QDialog):
    def __init__(self, teacher_dao: TeacherDAO):
        super().__init__()
        self.value = {}
        self.setWindowTitle('输入班级信息')
        layout = QFormLayout()

        self.class_name = QLineEdit(self)
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

        layout.addRow('班级名:', self.class_name)
        layout.addRow('所属老师', self.teacher_username)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)


    def accept(self):
        class_name = self.class_name.text()
        teacher_username = self.teacher_username.currentText()
        if class_name != '' and teacher_username != '':
            self.value['class_name'] = class_name
            self.value['teacher_username'] = teacher_username
        super().accept()

    def reject(self):
        super().reject()

    def get_value(self):
        return self.value






