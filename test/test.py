from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                                 QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QRadioButton)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class FaceRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition System")

        # Main layout
        main_layout = QHBoxLayout()

        # Left: Camera view
        self.camera_view = QLabel("摄像头捕获画面")
        self.camera_view.setFixedSize(640, 480)
        self.camera_view.setStyleSheet("border: 2px solid red;")
        self.camera_view.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.camera_view)

        # Right: Info and Controls
        right_layout = QVBoxLayout()

        # Face preview
        self.face_preview = QLabel("捕获的人脸")
        self.face_preview.setFixedSize(200, 200)
        self.face_preview.setStyleSheet("border: 2px solid red;")
        self.face_preview.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(self.face_preview, alignment=Qt.AlignCenter)

        # Form for user input
        form_group = QGroupBox("人脸信息")
        form_layout = QGridLayout()

        self.name_label = QLabel("姓名:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("请输入姓名")

        self.gender_label = QLabel("性别:")
        self.male_radio = QRadioButton("男")
        self.female_radio = QRadioButton("女")

        self.age_label = QLabel("年龄:")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("请输入年龄")

        form_layout.addWidget(self.name_label, 0, 0)
        form_layout.addWidget(self.name_input, 0, 1)

        form_layout.addWidget(self.gender_label, 1, 0)
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        form_layout.addLayout(gender_layout, 1, 1)

        form_layout.addWidget(self.age_label, 2, 0)
        form_layout.addWidget(self.age_input, 2, 1)

        form_group.setLayout(form_layout)
        right_layout.addWidget(form_group)

        # Buttons for actions
        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("确认录入")
        self.confirm_button.setStyleSheet("background-color: green; color: white;")
        self.cancel_button = QPushButton("放弃")
        self.cancel_button.setStyleSheet("background-color: red; color: white;")
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        right_layout.addLayout(button_layout)

        # Start/Stop buttons
        action_layout = QHBoxLayout()
        self.start_button = QPushButton("开始录入")
        self.stop_button = QPushButton("停止录入")
        action_layout.addWidget(self.start_button)
        action_layout.addWidget(self.stop_button)
        right_layout.addLayout(action_layout)

        # Add right layout to main layout
        main_layout.addLayout(right_layout)

        # Set main layout to the window
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = FaceRecognitionApp()
    window.show()
    app.exec()