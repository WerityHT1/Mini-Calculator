from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
class Ui_Window(object):
    
    res = "0"

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(300, 380)
        Window.setMinimumSize(QtCore.QSize(300, 380))
        Window.setMaximumSize(QtCore.QSize(300, 380))
        Window.setStyleSheet("QObject {\n"
"    background-color: rgb(18, 20, 18)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=Window)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 300, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.btn_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 320, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_0.setFlat(True)
        self.btn_0.setObjectName("btn_0")
        self.btn_dot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(75, 320, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_dot.setIconSize(QtCore.QSize(32, 32))
        self.btn_dot.setFlat(True)
        self.btn_dot.setObjectName("btn_dot")
        self.btn_C = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_C.setGeometry(QtCore.QRect(150, 320, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_C.setFont(font)
        self.btn_C.setStyleSheet("QPushButton {\n"
"    background-color: rgb(175, 175, 175); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 2px solid rgb(135, 135, 135);  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_C.setFlat(True)
        self.btn_C.setObjectName("btn_C")
        self.btn_equal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(225, 320, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("QPushButton {\n"
"    background-color: rgb(208, 13, 42); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 2px solid rgb(184, 12, 37);  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_equal.setFlat(True)
        self.btn_equal.setObjectName("btn_equal")
        self.btn_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(225, 260, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 199, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 2px solid rgb(231, 180, 27);  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_plus.setFlat(True)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(150, 260, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_3.setFlat(True)
        self.btn_3.setObjectName("btn_3")
        self.btn_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 260, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_1.setFlat(True)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(75, 260, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_2.setFlat(True)
        self.btn_2.setObjectName("btn_2")
        self.btn_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(75, 140, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_8.setFlat(True)
        self.btn_8.setObjectName("btn_8")
        self.btn_mul = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_mul.setGeometry(QtCore.QRect(225, 140, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_mul.setFont(font)
        self.btn_mul.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 199, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 2px solid rgb(231, 180, 27);  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_mul.setFlat(True)
        self.btn_mul.setObjectName("btn_mul")
        self.btn_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(150, 200, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_6.setFlat(True)
        self.btn_6.setObjectName("btn_6")
        self.btn_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(150, 140, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_9.setFlat(True)
        self.btn_9.setObjectName("btn_9")
        self.btn_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 140, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_7.setFlat(True)
        self.btn_7.setObjectName("btn_7")
        self.btn_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 200, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_4.setFlat(True)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(75, 200, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_5.setFlat(True)
        self.btn_5.setObjectName("btn_5")
        self.btn_min = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_min.setGeometry(QtCore.QRect(225, 200, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_min.setFont(font)
        self.btn_min.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 199, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 2px solid rgb(231, 180, 27);  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_min.setFlat(True)
        self.btn_min.setObjectName("btn_min")
        self.btn_back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(0, 80, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_back.setAutoDefault(False)
        self.btn_back.setDefault(False)
        self.btn_back.setFlat(True)
        self.btn_back.setObjectName("btn_back")
        self.btn_close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(150, 80, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_close.setFlat(True)
        self.btn_close.setObjectName("btn_close")
        self.btn_div = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(225, 80, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 199, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 2px solid rgb(231, 180, 27);  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_div.setFlat(True)
        self.btn_div.setObjectName("btn_div")
        self.btn_open = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(75, 80, 75, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_open.setFont(font)
        self.btn_open.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30); /* Черный фон */\n"
"    color: white;            /* Белый текст */\n"
"    border: 1px solid #333;  /* Темная граница для контраста */\n"
"    border-radius: 5px;      /* Скруглённые углы */\n"
"    padding: 5px 10px;       /* Внутренние отступы */\n"
"    font-weight: bold;       /* Жирный шрифт */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333;  /* Более темный при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;  /* Еще темнее при нажатии */\n"
"    color: #ccc;             /* Светлее текст при нажатии */\n"
"}")
        self.btn_open.setFlat(True)
        self.btn_open.setObjectName("btn_open")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 50px;\n"
"    margin-left: 1px;\n"
"    color: white;\n"
"}")
        self.label.setObjectName("label")
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        
        self.btn_1.clicked.connect(lambda: self.add_num("1"))
        self.btn_2.clicked.connect(lambda: self.add_num("2"))
        self.btn_3.clicked.connect(lambda: self.add_num("3"))
        self.btn_4.clicked.connect(lambda: self.add_num("4"))
        self.btn_5.clicked.connect(lambda: self.add_num("5"))
        self.btn_6.clicked.connect(lambda: self.add_num("6"))
        self.btn_7.clicked.connect(lambda: self.add_num("7"))
        self.btn_8.clicked.connect(lambda: self.add_num("8"))
        self.btn_9.clicked.connect(lambda: self.add_num("9"))
        self.btn_0.clicked.connect(lambda: self.add_num("0"))
        self.btn_mul.clicked.connect(lambda: self.add_num("*"))
        self.btn_div.clicked.connect(lambda: self.add_num("/"))
        self.btn_plus.clicked.connect(lambda: self.add_num("+"))
        self.btn_min.clicked.connect(lambda: self.add_num("-"))
        self.btn_C.clicked.connect(lambda: self.clear())
        self.btn_back.clicked.connect(lambda: self.backspace())
        self.btn_open.clicked.connect(lambda: self.add_num("("))
        self.btn_close.clicked.connect(lambda: self.add_num(")"))
        self.btn_equal.clicked.connect(lambda: self.calc())
        self.btn_dot.clicked.connect(lambda: self.add_num("."))

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Calculator"))
        self.btn_0.setText(_translate("Window", "0"))
        self.btn_dot.setText(_translate("Window", "."))
        self.btn_C.setText(_translate("Window", "C"))
        self.btn_equal.setText(_translate("Window", "="))
        self.btn_plus.setText(_translate("Window", "+"))
        self.btn_3.setText(_translate("Window", "3"))
        self.btn_1.setText(_translate("Window", "1"))
        self.btn_2.setText(_translate("Window", "2"))
        self.btn_8.setText(_translate("Window", "8"))
        self.btn_mul.setText(_translate("Window", "*"))
        self.btn_6.setText(_translate("Window", "6"))
        self.btn_9.setText(_translate("Window", "9"))
        self.btn_7.setText(_translate("Window", "7"))
        self.btn_4.setText(_translate("Window", "4"))
        self.btn_5.setText(_translate("Window", "5"))
        self.btn_min.setText(_translate("Window", "-"))
        self.btn_back.setText(_translate("Window", "<-"))
        self.btn_close.setText(_translate("Window", ")"))
        self.btn_div.setText(_translate("Window", "/"))
        self.btn_open.setText(_translate("Window", "("))
        self.label.setText(_translate("Window", "0"))

    def add_num(self, num):
        if self.res == "0":
            self.res = num
        else:
            self.res += num;
        self.label.setText(self.res)

    def calc(self):
        try:
            self.res = str(eval(self.res))
            self.label.setText(self.res)
        except Exception:
            self.label.setText("Ошибка")
            self.res = "0"

    def clear(self):
        self.res = "0";
        self.label.setText(self.res);
    
    def backspace(self):
        if len(self.res) > 1:
            self.res = self.res[:-1]
        else:
            self.res = "0"
        self.label.setText(self.res)


if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    base_path = sys._MEIPASS
    icon_path = os.path.join(base_path, "Calculator-icon.ico")
    Window.setWindowIcon(QIcon(icon_path))
    Window.show()
    sys.exit(app.exec())
