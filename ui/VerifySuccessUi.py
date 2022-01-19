# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VerifySuccessUi.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_VerifySuccess(object):
    def setupUi(self, VerifySuccess):
        if not VerifySuccess.objectName():
            VerifySuccess.setObjectName(u"VerifySuccess")
        VerifySuccess.resize(151, 121)
        self.verticalLayout = QVBoxLayout(VerifySuccess)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(VerifySuccess)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(VerifySuccess)

        QMetaObject.connectSlotsByName(VerifySuccess)
    # setupUi

    def retranslateUi(self, VerifySuccess):
        VerifySuccess.setWindowTitle(QCoreApplication.translate("VerifySuccess", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("VerifySuccess", u"\u767b\u5f55\u6210\u529f", None))
    # retranslateUi

