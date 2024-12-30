from PySide6.QtWidgets import (
    QMainWindow
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
        
        self.teacher_dao = TeacherDAO(self.db)
        self.teacher_table_model = TeacherTableModel(self.teacher_dao)
        self.table_view_teachers.setModel(self.teacher_table_model)

        self.class_dao = ClassDAO(self.db)
        self.class_table_model = ClassTableModel(self.class_dao)
        self.table_view_classes.setModel(self.class_table_model)

        #绑定功能切换
        self.stacked_widget.setCurrentIndex(0)
        self.tree_widget.itemClicked.connect(self.on_tree_widget_clicked)
        


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




