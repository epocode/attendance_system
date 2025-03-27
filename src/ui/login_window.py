from src.ui.ui_files.ui_login import Ui_Form
from PySide6.QtWidgets import QWidget, QMessageBox, QDialog, QFormLayout, QLineEdit, QPushButton
from PySide6.QtCore import QEventLoop
from src.db.database import DataBase
from src.db.teacher_dao import TeacherDAO
from src.ui.admin_window import AdminWindow


class LoginWindow(Ui_Form, QWidget):
    def __init__(self, db=None, main_window=None):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('登陆')
        
        if db is None:
            self.db = DataBase()
        else:
            self.db = db
        
        self.teacher_dao = TeacherDAO(self.db)

        if main_window is None:
            self.btn_login.clicked.connect(self.login)

        else:
            self.main_window = main_window
            self.btn_login.clicked.connect(self.change_user)

        
        self.btn_register.clicked.connect(self.register)
        self.btn_admin.clicked.connect(self.enter_admin)
        

    def change_user(self):
        username = self.line_edit_uername.text()
        pswd = self.line_edit_pswd.text()
        res = self.teacher_dao.check_login(username, pswd)
        if res is None:
            QMessageBox.warning(self, '登陆失败', '当前用户名不存在或者密码错误')
            return False

        teacher_name, username = res

        
        self.main_window.change_user(teacher_name, username)
        self.close()
    
    def login(self):
        username = self.line_edit_uername.text()
        pswd = self.line_edit_pswd.text()
        res = self.teacher_dao.check_login(username, pswd)
        if res is None:
            QMessageBox.warning(self, '登陆失败', '当前用户名不存在或者密码错误')
            return False

        teacher_name, username = res

        from src.ui.main_window import MainWindow
        self.main_window = MainWindow(teacher_name, username, self.db)
        self.main_window.show()
        self.close()

    def register(self):
        input_dialog = InputDialog()
        if input_dialog.exec() == QDialog.Accepted:
            name, username, pswd = input_dialog.get_user_data()
            res = self.teacher_dao.register(name, username, pswd)
            if res is False:
                QMessageBox.warning(self, '注册失败', '当前用户名已存在')
            else:
                QMessageBox.information(self, '注册成功', '注册成功，请登陆')

    def enter_admin(self):
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.close()
            
    def exec_(self):
        self._event_loop = QEventLoop()
        self.show()
        self._event_loop.exec_()
        
class InputDialog(QDialog):
    def __init__(self):
        super().__init__()

        # 设置对话框标题
        self.setWindowTitle("注册")

        # 创建布局
        layout = QFormLayout()

        # 创建三个 QLineEdit 输入框
        self.name_input = QLineEdit(self)
        self.username_input = QLineEdit(self)
        self.pswd_input = QLineEdit(self)
        self.pswd_input.setEchoMode(QLineEdit.Password)

        # 创建按钮
        self.submit_button = QPushButton("提交", self)
        self.submit_button.clicked.connect(self.submit)

        # 将控件添加到布局中
        layout.addRow("姓名:", self.name_input)
        layout.addRow("用户名:", self.username_input)
        layout.addRow("密码:", self.pswd_input)
        layout.addWidget(self.submit_button)

        # 设置对话框的布局
        self.setLayout(layout)

        # 用于存储用户输入的信息
        self.user_data = None

    def submit(self):
        # 获取用户输入的数据
        name = self.name_input.text()
        username = self.username_input.text()
        pswd = self.pswd_input.text()

        # 将数据存储到对象中
        self.user_data = (name, username, pswd)

        # 关闭对话框
        self.accept()

    def get_user_data(self):
        return self.user_data
        
