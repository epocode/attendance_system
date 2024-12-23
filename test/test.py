from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout, QPushButton, QListView, QStackedWidget, QHBoxLayout
from PySide6.QtCore import Qt, QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建分割器
        splitter = QSplitter(Qt.Horizontal)

        # 创建左侧的功能选项
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        list_view = QListView()
        options = QStringListModel(["功能1", "功能2", "功能3"])
        list_view.setModel(options)
        left_layout.addWidget(list_view)

        # 创建右侧的内容显示区域
        right_widget = QStackedWidget()
        page1 = QWidget()
        page2 = QWidget()
        page3 = QWidget()

        # 在右侧页面上添加内容
        page1_layout = QVBoxLayout(page1)
        page1_layout.addWidget(QPushButton("这是功能1的界面"))

        page2_layout = QVBoxLayout(page2)
        page2_layout.addWidget(QPushButton("这是功能2的界面"))

        page3_layout = QVBoxLayout(page3)
        page3_layout.addWidget(QPushButton("这是功能3的界面"))

        # 添加页面到 QStackedWidget
        right_widget.addWidget(page1)
        right_widget.addWidget(page2)
        right_widget.addWidget(page3)

        # 将左右布局添加到分割器
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        # 将分割器设置为主窗口的中央部件
        self.setCentralWidget(splitter)

        # 当点击列表选项时，切换右侧界面的内容
        list_view.selectionModel().currentChanged.connect(self.on_option_selected)

    def on_option_selected(self, index):
        selected_option = index.data()
        if selected_option == "功能1":
            self.centralWidget().widget(1).setCurrentIndex(0)  # 显示第一个界面
        elif selected_option == "功能2":
            self.centralWidget().widget(1).setCurrentIndex(1)  # 显示第二个界面
        elif selected_option == "功能3":
            self.centralWidget().widget(1).setCurrentIndex(2)  # 显示第三个界面

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
