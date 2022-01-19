# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VerifyFalseUi.ui'
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

class Ui_Verify_False(object):
    def setupUi(self, Verify_False):
        if not Verify_False.objectName():
            Verify_False.setObjectName(u"Verify_False")
        Verify_False.resize(276, 169)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Verify_False.sizePolicy().hasHeightForWidth())
        Verify_False.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        Verify_False.setFont(font)
        Verify_False.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Verify_False)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Verify_False)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Verify_False)

        QMetaObject.connectSlotsByName(Verify_False)
    # setupUi

    def retranslateUi(self, Verify_False):
        Verify_False.setWindowTitle(QCoreApplication.translate("Verify_False", u"\u767b\u5f55\u6210\u529f", None))
        self.label.setText(QCoreApplication.translate("Verify_False", u"\u767b\u5f55\u5931\u8d25\uff0c\u8bf7\u68c0\u67e5\u8d26\u53f7\u5bc6\u7801\uff01", None))
    # retranslateUi

