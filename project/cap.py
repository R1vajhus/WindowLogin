from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import QTimer
import random, string

class CapchaWindow(QWidget):
    def __init__(self):
        super().__init__()
        len = 5
        capcha = string.ascii_uppercase + string.digits
        rnd = ''.join(random.sample(capcha, len))
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.lbl_cap = QLabel(str(rnd))
        self.lbl_cap.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_cap.setObjectName("capch")
        self.line = QLineEdit()
        self.btn = QPushButton("Push")
        self.btn.clicked.connect(self.btn_c)
        self.lbl_timer = QLabel()
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(self.lbl_cap)
        vbox.addWidget(self.line)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.lbl_timer)
        with open("styles\style_cap.css", "r") as css:
            self.setStyleSheet(css.read())
        self.conter = 0
        
        
    def btn_c(self):
        len = 5
        capcha = string.ascii_uppercase + string.digits
        rnd = ''.join(random.sample(capcha, len))
        if self.line.text() == self.lbl_cap.text():
            self.close()
        else:
            self.lbl_cap.setText(str(rnd))
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.timer_r)
            self.timer.start()
            self.conter += 1
            if self.conter == 1:
                self.seconds = 10
            if self.conter == 2:
                self.seconds = 15
            if self.conter > 2:
                self.seconds = 30
        
        
    def timer_r(self):
        self.seconds -= 1
        self.lbl_timer.setText(str(self.seconds))
        if self.seconds == 0:
            self.timer.stop()
            self.lbl_timer.setText("")
