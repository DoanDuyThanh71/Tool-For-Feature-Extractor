import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Home import Ui_MainWindow
import os 
from PyQt6.QtWidgets import QGraphicsOpacityEffect, QLabel

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        original_image = QtGui.QPixmap("logo_haui.webp")
        
        # Tạo QLabel để hiển thị hình ảnh
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setGeometry(60, 0, 500, 100)
        self.imageLabel.setPixmap(original_image)
        scaled_image = original_image.scaled(original_image.size() / 1.8, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imageLabel.setPixmap(scaled_image)
        
        # Label title
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(150, 90, 100, 30))
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setText("LOGIN")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)
        
        # Label subtitle
        self.label_subtitle = QtWidgets.QLabel(self.centralwidget)
        self.label_subtitle.setGeometry(QtCore.QRect(120, 120, 160, 20))
        self.label_subtitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_subtitle.setText("Please sign in to continue")
        
        # Email input
        self.userName = QtWidgets.QLineEdit(self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(50, 170, 300, 40))
        self.userName.setPlaceholderText("Username")
        self.userName.setClearButtonEnabled(True)
        self.userName.setStyleSheet("QLineEdit { padding-left: 30px; }")
        self.userName.setText("")
        email_icon = QtGui.QIcon('img_user.png')
        self.userName.addAction(email_icon, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        
        # Password input
        self.text_password = QtWidgets.QLineEdit(self.centralwidget)
        self.text_password.setGeometry(QtCore.QRect(50, 220, 300, 40))
        self.text_password.setPlaceholderText("Password")
        self.text_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.text_password.setClearButtonEnabled(True)
        self.text_password.setStyleSheet("QLineEdit { padding-left: 30px; }")
        password_icon = QtGui.QIcon("img_padlock.png")
        self.text_password.addAction(password_icon, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        
        # Login button
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(150, 290, 100, 40))
        self.btn_login.setText("Log In")
        self.btn_login.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 14px; }")
        self.btn_login.clicked.connect(self.check_login)
        
        # Status label
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(50, 270, 300, 30))
        self.label_status.setText("")
        self.label_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        MainWindow.setFixedSize(400, 380)  # Khóa kích thước cửa sổ
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
    
    def check_login(self):
        username = self.userName.text()
        password = self.text_password.text()
        
        # Đọc tệp users.txt và kiểm tra thông tin đăng nhập
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
                
                for user in users:
                    user = user.strip().split(":")
                    if user[0] == username and user[1] == password:
                        self.label_status.setText("Login successful!")
                        self.open_home_window()
                        return
                        
                self.label_status.setText("Invalid username or password.")
        
        except FileNotFoundError:
            self.label_status.setText("Error: users.txt file not found.")
        except Exception as e:
            self.label_status.setText(f"An error occurred: {e}")

    def open_home_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
          

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec())
