# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(457, 361)
        self.verticalLayout_3 = QVBoxLayout(LoginWindow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.logo = QLabel(LoginWindow)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.logo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 40, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UserLabel = QLabel(LoginWindow)
        self.UserLabel.setObjectName(u"UserLabel")
        sizePolicy.setHeightForWidth(self.UserLabel.sizePolicy().hasHeightForWidth())
        self.UserLabel.setSizePolicy(sizePolicy)
        self.UserLabel.setBaseSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(14)
        self.UserLabel.setFont(font)
        self.UserLabel.setLayoutDirection(Qt.LeftToRight)
        self.UserLabel.setScaledContents(True)
        self.UserLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.UserLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.PasswordLabel = QLabel(LoginWindow)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        sizePolicy.setHeightForWidth(self.PasswordLabel.sizePolicy().hasHeightForWidth())
        self.PasswordLabel.setSizePolicy(sizePolicy)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setLayoutDirection(Qt.LeftToRight)
        self.PasswordLabel.setScaledContents(True)
        self.PasswordLabel.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.verticalLayout.addWidget(self.PasswordLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.UserName = QLineEdit(LoginWindow)
        self.UserName.setObjectName(u"UserName")
        sizePolicy.setHeightForWidth(self.UserName.sizePolicy().hasHeightForWidth())
        self.UserName.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.UserName)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.Password = QLineEdit(LoginWindow)
        self.Password.setObjectName(u"Password")
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        self.Password.setInputMethodHints(Qt.ImhDate)
        self.Password.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.Password)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 30, -1, 30)
        self.Verify_Btn = QPushButton(LoginWindow)
        self.Verify_Btn.setObjectName(u"Verify_Btn")
        sizePolicy.setHeightForWidth(self.Verify_Btn.sizePolicy().hasHeightForWidth())
        self.Verify_Btn.setSizePolicy(sizePolicy)
        self.Verify_Btn.setFont(font)

        self.horizontalLayout.addWidget(self.Verify_Btn)

        self.Login_Btn = QPushButton(LoginWindow)
        self.Login_Btn.setObjectName(u"Login_Btn")
        sizePolicy.setHeightForWidth(self.Login_Btn.sizePolicy().hasHeightForWidth())
        self.Login_Btn.setSizePolicy(sizePolicy)
        self.Login_Btn.setFont(font)

        self.horizontalLayout.addWidget(self.Login_Btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"\u767b\u5f55\u9a8c\u8bc1", None))
        self.logo.setText(QCoreApplication.translate("LoginWindow", u"TextLabel", None))
        self.UserLabel.setText(QCoreApplication.translate("LoginWindow", u"\u7528\u6237\u540d", None))
        self.PasswordLabel.setText(QCoreApplication.translate("LoginWindow", u"\u5bc6 \u7801", None))
        self.Verify_Btn.setText(QCoreApplication.translate("LoginWindow", u"\u9a8c\u8bc1", None))
        self.Login_Btn.setText(QCoreApplication.translate("LoginWindow", u"\u767b\u5f55", None))
    # retranslateUi

