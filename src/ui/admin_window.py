from PySide6.QtWidgets import (
    QMainWindow,
    QDialog,
    QFormLayout,
    QLineEdit,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QAbstractItemView,
)
from src.ui.ui_files.ui_admin_window import Ui_AdminWindow
from src.db.database import DataBase
from src.db.teacher_dao import TeacherDAO
from src.data_model.teacher_table_model import TeacherTableModel
from src.db.class_dao import ClassDAO
from src.data_model.class_table_model import ClassTableModel

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
        

        #绑定功能切换
        self.stacked_widget.setCurrentIndex(0)
        self.tree_widget.itemClicked.connect(self.on_tree_widget_clicked)
        

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
            

    def on_delete_teacher_clicked(self):
        selected_indexes = self.table_view_teachers.selectionModel().selectedRows()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            self.teacher_dao.delete_row(selected_row)
            self.teacher_table_model.layoutChanged.emit()


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






