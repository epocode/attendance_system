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
from ui_main_window import Ui_MainWindow
import resources
import sys
import cv2
from ultralytics import YOLO
import torch
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config.my_config as my_config
from face_take import FaceTaker
from src.data_model.db_name_list import TableNameListModel, personInfoModel
    
class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


        self.stackedWidget.setCurrentIndex(0)

        #statusbar 
        self.status_bar = self.statusBar()

        #toolbar
        self.toolbar = self.addToolBar("tool bar")
        self.toolbar
        
        action_back_home = QAction(QIcon(":/icons/home"), 'home', self)
        action_back_home.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.toolbar.addAction(action_back_home)

        #数据库的创建
        self.list_model_tables = TableNameListModel()
        self.listview_table_select.setModel(self.list_model_tables)
        
        self.label_curtable = QLabel("未选择表格")
        self.status_bar.addWidget(self.label_curtable)
        self.btn_confirm_table.clicked.connect(self.confirm_table)

        self.person_info_model = None

        self.btn_create_table.clicked.connect(self.create_new_table)
        self.btn_drop_table.clicked.connect(self.drop_table)
        

        #将工具栏停放到左侧
        dock  = QDockWidget()
        dock.setWidget(self.toolbar)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        # 人脸的录入
        self.face_taker = None
        self.cur_face = None

        #连接槽函数
        self.btn_collect_face.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_face_detect.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_start.clicked.connect(self.start_show_video)
        self.btn_end.clicked.connect(self.end_show_video)

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


    def face_get(self, qimage):
        self.cur_face = qimage
        pixmap = QPixmap.fromImage(qimage)
        self.label_face.setPixmap(pixmap)
    
    def closeEvent(self, event):
        self.end_show_video()
        super().closeEvent(event)
        #记得关闭所有的数据库连接

    def confirm_table(self):
        selected_indexes = self.listview_table_select.selectedIndexes()
        if selected_indexes:
            for index in selected_indexes:
                table_name = self.list_model_tables.data(index, Qt.DisplayRole)
                self.label_curtable.setText(f"current table:{table_name}")
                self.list_model_tables.cur_table_name = table_name
                self.person_info_model = personInfoModel(self.list_model_tables.conn, self.list_model_tables.cur_table_name)
                self.table_view_show_stu.setModel(self.person_info_model)

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
        self.person_info_model.insert_data(name, gender, age, face_feature)

        self.face_taker.resume()
        
        #录取完这张图片后，就禁止再点击录入按钮
        self.cur_face = None


    def create_new_table(self):
        text, ok = QInputDialog.getText(self, '输入表名', '表名', QLineEdit.Normal)
        if ok and text:
            self.list_model_tables.create_new_table(text)
        else:
            print('取消新表的创建')

    def drop_table(self):
        selected_indexes = self.listview_table_select.selectedIndexes()
        if len(selected_indexes) != 0:
            for idx in selected_indexes:
                table_name = self.list_model_tables.data(idx, Qt.DisplayRole)
                self.list_model_tables.drop_selected_table(table_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    app.exec()