import sys
from PyQt6.QtWidgets import QLabel,QApplication, QWidget,QLineEdit,QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QStackedLayout, QRadioButton, QComboBox, QCheckBox
from PyQt6 import QtCore
from cap import CapchaWindow
from sqlalchemy import text, create_engine
from sqlalchemy.orm import create_session


#Engine Database___________________
engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/foir")
session = create_session(bind=engine)

class Auth():
    def isLogin(login, password):
        a = session.execute(text(f"SELECT * FROM auth WHERE login='{login}'")).fetchall()
        session.commit()
        session.close()
        for i in a:
            if login == i[1]:
                if password == i[2]:
                    return True
                else:
                    continue
            else:
                return False

#MainWindow___________________
class  MainWindow(QMainWindow, Auth):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        vbox = QVBoxLayout()
    
        button = QPushButton("Auth")
        button.clicked.connect(self.btn)
    
        btn_back = QPushButton("Quit")
        btn_back.clicked.connect(self.btn_quit)
        
        lbl_log = QLabel("Login")
        lbl_pass = QLabel("Password")
        self.line_log = QLineEdit("Oleg")
        self.line_pass = QLineEdit("1234")
        
        
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbox)
        
        
        vbox.addWidget(lbl_log)
        vbox.addWidget(self.line_log)
        vbox.addWidget(lbl_pass)
        vbox.addWidget(self.line_pass)
        vbox.addWidget(button)
        vbox.addWidget(btn_back)
        
        
    def btn(self):
        if Auth.isLogin(self.line_log.text(), self.line_pass.text()):
            self.welcome = WelcomeWindow()
            self.welcome.show()
            self.close()
        else:
            self.cap = CapchaWindow()
            self.cap.show()
    
    def btn_quit(self):
        quit()
        
#Welcome Window___________________
class  WelcomeWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        lbl = QLabel("Добро пожаловать на минитест!")
        btn = QPushButton("Погнали")
        btn.clicked.connect(self.click_b)
        vbox = QVBoxLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbox)
        vbox.addWidget(lbl)
        vbox.addWidget(btn)
        with open("styles\style.css", "r") as css:
            self.setStyleSheet(css.read())
            
    def click_b(self):
        self.test = TestWindow()
        self.test.show()
        self.close()
            



#Test Window___________________
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,150)
        lbl1 = QLabel("1.Какая главная валюта в Евросозе?")
        self.rb1 = QRadioButton(text="Евро")
        rb2 = QRadioButton(text="Рубль")
        rb3 = QRadioButton(text="Юань")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(rb3)

        lbl2 = QLabel("2.Какой национальный цветок Японии?")
        rb1_1 = QRadioButton(text="Клён")
        self.rb2_1 = QRadioButton(text="Сакура")
        rb3_1 = QRadioButton(text="Дуб")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(lbl2)
        vbox2.addWidget(rb1_1)
        vbox2.addWidget(self.rb2_1)
        vbox2.addWidget(rb3_1)
 
        lbl3 = QLabel("3.Сколько полос на флаге США?")
        self.rb1_2 = QRadioButton(text="13")
        rb2_2 = QRadioButton(text="15")
        rb3_2 = QRadioButton(text="11")
        vbox3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox3)
        vbox3.addWidget(lbl3)
        vbox3.addWidget(self.rb1_2)
        vbox3.addWidget(rb2_2)
        vbox3.addWidget(rb3_2)
        
        lbl4 = QLabel("4.Какая расшифровка у химической формулы H2O?")
        rb1_3 = QRadioButton(text="Спирт")
        rb2_3 = QRadioButton(text="Серная кислота")
        self.rb3_3 = QRadioButton(text="Вода")
        vbox4 = QVBoxLayout()
        widget4 = QWidget()
        widget4.setLayout(vbox4)
        vbox4.addWidget(lbl4)
        vbox4.addWidget(rb1_3)
        vbox4.addWidget(rb2_3)
        vbox4.addWidget(self.rb3_3)
        
        lbl5 = QLabel("5.Какой самый распространенный язык в мире?")
        rb1_4 = QRadioButton(text="Английский")
        self.rb2_4 = QRadioButton(text="Китайский")
        rb3_4 = QRadioButton(text="Испаниский")
        vbox5 = QVBoxLayout()
        widget5 = QWidget()
        widget5.setLayout(vbox5)
        vbox5.addWidget(lbl5)
        vbox5.addWidget(rb1_4)
        vbox5.addWidget(self.rb2_4)
        vbox5.addWidget(rb3_4)
        
        lbl9 = QLabel("6.Что из предложенного является валютой?")
        self.rb1_9 = QCheckBox(text="Тугрик")
        self.rb2_9 = QCheckBox(text="Биткоин")
        self.rb3_9 = QCheckBox(text="Лев")
        vbox9 = QVBoxLayout()
        widget9 = QWidget()
        widget9.setLayout(vbox9)
        vbox9.addWidget(lbl9)
        vbox9.addWidget(self.rb1_9)
        vbox9.addWidget(self.rb2_9)
        vbox9.addWidget(self.rb3_9)
        
        lbl90 = QLabel("7.Что из предложенного является языком программирования?")
        self.rb1_90 = QCheckBox(text="С+-")
        self.rb2_90 = QCheckBox(text="Dart")
        self.rb3_90 = QCheckBox(text="F#")
        vbox90 = QVBoxLayout()
        widget90 = QWidget()
        widget90.setLayout(vbox90)
        vbox90.addWidget(lbl90)
        vbox90.addWidget(self.rb1_90)
        vbox90.addWidget(self.rb2_90)
        vbox90.addWidget(self.rb3_90)
        
        lbl6 = QLabel("Готовы увидеть свои результаты?")
        lbl6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        rb3_5 = QPushButton("Да")
        rb3_5.clicked.connect(self.activate_tab_v)
        rb3_5.clicked.connect(self.result)
        vbox6 = QVBoxLayout()
        widget6 = QWidget()
        widget6.setLayout(vbox6)
        vbox6.addWidget(lbl6)
        vbox6.addWidget(rb3_5)
        
        lbl7 = QLabel("Результаты теста:")
        self.v6 = QLabel()
        self.v2 = QLabel()
        self.v3 = QLabel()
        self.v4 = QLabel()
        self.v5 = QLabel()
        self.v7 = QLabel()
        self.v8 = QLabel()
        self.v6_1 = QLabel("Вопрос №1: ")
        self.v2_1 = QLabel("Вопрос №2: ")
        self.v3_1 = QLabel("Вопрос №3: ")
        self.v4_1 = QLabel("Вопрос №4: ")
        self.v5_1 = QLabel("Вопрос №5: ")
        self.v7_1 = QLabel("Вопрос №6: ")
        self.v8_1 = QLabel("Вопрос №7: ")
        self.res = QLabel()
        self.name_file = QLineEdit()
        self.type = QComboBox()
        self.type.addItem(".txt")
        save = QPushButton("Сохранить результаты")
        save.clicked.connect(self.load)
        hboxv1 = QHBoxLayout()
        hboxv1.addWidget(self.v6_1)
        hboxv1.addWidget(self.v6)
        hboxv2 = QHBoxLayout()
        hboxv2.addWidget(self.v2_1)
        hboxv2.addWidget(self.v2)
        hboxv3 = QHBoxLayout()
        hboxv3.addWidget(self.v3_1)
        hboxv3.addWidget(self.v3)
        hboxv4 = QHBoxLayout()
        hboxv4.addWidget(self.v4_1)
        hboxv4.addWidget(self.v4)
        hboxv5 = QHBoxLayout()
        hboxv5.addWidget(self.v5_1)
        hboxv5.addWidget(self.v5)
        hboxv7 = QHBoxLayout()
        hboxv7.addWidget(self.v7_1)
        hboxv7.addWidget(self.v7)
        hboxv8 = QHBoxLayout()
        hboxv8.addWidget(self.v8_1)
        hboxv8.addWidget(self.v8)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.name_file)
        hbox1.addWidget(self.type)
        vbox7 = QVBoxLayout()
        widget7 = QWidget()
        widget7.setLayout(vbox7)
        vbox7.addWidget(lbl7)
        vbox7.addLayout(hboxv1)
        vbox7.addLayout(hboxv2)
        vbox7.addLayout(hboxv3)
        vbox7.addLayout(hboxv4)
        vbox7.addLayout(hboxv5)
        vbox7.addLayout(hboxv7)
        vbox7.addLayout(hboxv8)
        vbox7.addWidget(self.res)
        vbox7.addLayout(hbox1)
        vbox7.addWidget(save)

        
        

        pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(self.button_layout)
        
        self.btnb = QPushButton("back")
        self.btn = QPushButton("next")
        
        self.btnb.clicked.connect(self.activate_tab_b)
        self.btn.clicked.connect(self.activate_tab_v)
        self.stacklayout.addWidget(widget)
        self.button_layout.addWidget(self.btnb)
        self.button_layout.addWidget(self.btn)
        

        self.stacklayout.addWidget(widget2)

        self.stacklayout.addWidget(widget3)

        self.stacklayout.addWidget(widget4)

        self.stacklayout.addWidget(widget5)
        
        self.stacklayout.addWidget(widget9)
        
        self.stacklayout.addWidget(widget90)

        self.stacklayout.addWidget(widget6)
        
        self.stacklayout.addWidget(widget7)
        


        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
        
        with open("styles\style_second.css", "r") as css:
            self.setStyleSheet(css.read())

    def activate_tab_v(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)
            
    

    def activate_tab_b(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)
        
    def result(self, state):
        if self.rb1.isChecked():
            self.v6.setText("Верно")
            a = 1
        else: 
            self.v6.setText("Не верно")
            a = 0
        if self.rb2_1.isChecked():
            self.v2.setText("Верно")
            b = a + 1
        else:
            self.v2.setText("Не верно")
            b = a
        if self.rb1_2.isChecked():
            self.v3.setText("Верно")
            t = b + 1
        else:
            self.v3.setText("Не верно")
            t = b
        if self.rb3_3.isChecked():
            self.v4.setText("Верно")
            d = t + 1
        else:
            self.v4.setText("Не верно")
            d = t
        if self.rb2_4.isChecked():
            self.v5.setText("Верно")
            e = d + 1
        else:
            self.v5.setText("Не верно")
            e = d
            
        if self.rb1_9.isChecked() and self.rb3_9.isChecked():
            self.v7.setText("Верно")
            f = e + 1
        elif self.rb1_9.isChecked() or self.rb3_9.isChecked():
            self.v7.setText("Частично верно")
            f = e + 0.5
        elif self.rb1_9.isCheckable() and self.rb3_9.isCheckable():
            self.v7.setText("Не верно")
            f = e  
            
        if self.rb2_90.isChecked() and self.rb3_90.isChecked():
            self.v8.setText("Верно")
            self.g = f + 1
        elif self.rb2_90.isChecked() or self.rb3_90.isChecked():
            self.v8.setText("Частично верно")
            self.g = f + 0.5
        elif self.rb2_90.isCheckable() and self.rb3_90.isCheckable():
            self.v8.setText("Не верно")
            self.g = f    


            
        self.setFixedSize(450, 500)
        self.res.setText(f"Ваш результат:{self.g}")
            
    def load(self):
        if self.type.currentText() == ".txt":
            txt = f"{self.v6_1.text()}{self.v6.text()}\n"
            txt1 = f"{self.v2_1.text()}{self.v2.text()}\n"
            txt2 = f"{self.v3_1.text()}{self.v3.text()}\n"
            txt3 = f"{self.v4_1.text()}{self.v4.text()}\n"
            txt4 = f"{self.v5_1.text()}{self.v5.text()}\n"
            txt5 = f"{self.v7_1.text()}{self.v7.text()}\n"
            txt6 = f"{self.v8_1.text()}{self.v8.text()}\n"
            txt7 = f"Ваш результат:{self.g}"
            t = open(f"{self.name_file.text()}.txt", "w", encoding="utf-8")
            t.write(txt)
            t.write(txt1)
            t.write(txt2)
            t.write(txt3)
            t.write(txt4)
            t.write(txt5)
            t.write(txt6)
            t.write(txt7)
            t.close()
            
        
app = QApplication(sys.argv)
window = MainWindow()
with open("styles\style.css", "r") as css:
    window.setStyleSheet(css.read())
window.show()
app.exec()