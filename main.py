#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： LiuYuZhao
# datetime： 2022/1/19 13:54
import socket
import threading
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QMessageBox, QDialog
from ui.login import Ui_LoginWindow
from ui.Main import Ui_MainWindow
from ui.VerifySuccessUi import Ui_VerifySuccess
from ui.VerifyFalseUi import Ui_Verify_False
import time


class LoginWindow(QWidget):
    def __init__(self, IP, Port):
        super(LoginWindow, self).__init__()
        self.IP = IP
        self.Port = Port
        self.VerifyInfo = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.Password.setEchoMode(QLineEdit.Password)
        pixmap = QPixmap("image/logo.png")
        self.ui.logo.setPixmap(pixmap)
        self.ui.Verify_Btn.clicked.connect(self.verify)
        self.ui.Login_Btn.clicked.connect(self.verify_login)
        self.setWindowIcon(QIcon('./image/logo_big.png'))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.IP, self.Port)
        self.sock.connect(server_address)

    # verify
    # send user name and password to server
    # if not start receive thread start it
    def verify(self):
        self.user_name = self.ui.UserName.text()
        self.password = self.ui.Password.text()
        request_info = str(self.user_name) + '&' + str(self.password)

        self.sock.send(str(request_info).encode('utf-8'))
        start_receive = False
        if not start_receive:
            threading.Thread(target=self.receiveMsg).start()

    # receive from server
    def receiveMsg(self):
        while True:
            try:
                data = self.sock.recv(1024)
                record = data.decode('utf-8')
                print(record)
                if str(record) == str("True"):
                    print("logined")
                    self.VerifyInfo = True

                elif str(record) == str("False"):
                    print("password error")
                    self.VerifyInfo = False
            except:
                pass

    # main window
    def main_window(self):
        self.window = MainWindow()
        self.window.show()

    # when click login button
    def verify_login(self):
        if self.VerifyInfo == True:
            self.verify_ok = VerifySuccess()
            self.verify_ok.show()
            time.sleep(0.3)
            # open main window
            self.main_window()

        if self.VerifyInfo == False:
            self.verify_error = VerifyFalse()
            self.verify_error.show()


# Dialog of verify success
class VerifySuccess(QDialog):
    def __init__(self):
        super(VerifySuccess, self).__init__()
        self.ui = Ui_VerifySuccess()
        self.setWindowIcon(QIcon('./image/logo_big.png'))
        self.ui.setupUi(self)


# Dialog of verify false
class VerifyFalse(QDialog):
    def __init__(self):
        super(VerifyFalse, self).__init__()
        self.ui = Ui_Verify_False()
        self.setWindowIcon(QIcon('./image/logo_big.png'))
        self.ui.setupUi(self)


# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setWindowIcon(QIcon('./image/logo_big.png'))
        self.ui.setupUi(self)
        pixmap = QPixmap("image/logo_big.png")
        self.ui.mainlogo.setPixmap(pixmap)


# main program
if __name__ == "__main__":
    IP = "" # need change
    Port = 111 # need change
    app = QApplication([])
    main_window = LoginWindow(IP, Port)
    main_window.show()
    app.exec()
