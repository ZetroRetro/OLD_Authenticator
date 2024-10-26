# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginjexKRO.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        if not loginDialog.objectName():
            loginDialog.setObjectName(u"loginDialog")
        loginDialog.resize(369, 192)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginDialog.sizePolicy().hasHeightForWidth())
        loginDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(loginDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.loginLabel = QLabel(loginDialog)
        self.loginLabel.setObjectName(u"loginLabel")

        self.verticalLayout_4.addWidget(self.loginLabel)

        self.loginEdit = QLineEdit(loginDialog)
        self.loginEdit.setObjectName(u"loginEdit")

        self.verticalLayout_4.addWidget(self.loginEdit)

        self.passwordLabel = QLabel(loginDialog)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.verticalLayout_4.addWidget(self.passwordLabel)

        self.passwordEdit = QLineEdit(loginDialog)
        self.passwordEdit.setObjectName(u"passwordEdit")

        self.verticalLayout_4.addWidget(self.passwordEdit)

        self.showPasswordBox = QCheckBox(loginDialog)
        self.showPasswordBox.setObjectName(u"showPasswordBox")

        self.verticalLayout_4.addWidget(self.showPasswordBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.loginButton = QPushButton(loginDialog)
        self.loginButton.setObjectName(u"loginButton")

        self.horizontalLayout_4.addWidget(self.loginButton)

        self.registerButton = QPushButton(loginDialog)
        self.registerButton.setObjectName(u"registerButton")

        self.horizontalLayout_4.addWidget(self.registerButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.StatusLabel = QLabel(loginDialog)
        self.StatusLabel.setObjectName(u"StatusLabel")

        self.horizontalLayout_4.addWidget(self.StatusLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(loginDialog)

        QMetaObject.connectSlotsByName(loginDialog)
    # setupUi

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QCoreApplication.translate("loginDialog", u"Login", None))
        self.loginLabel.setText(QCoreApplication.translate("loginDialog", u"Login:", None))
        self.passwordLabel.setText(QCoreApplication.translate("loginDialog", u"Password:", None))
        self.showPasswordBox.setText(QCoreApplication.translate("loginDialog", u"Show Password", None))
        self.loginButton.setText(QCoreApplication.translate("loginDialog", u"Login", None))
        self.registerButton.setText(QCoreApplication.translate("loginDialog", u"Register", None))
        self.StatusLabel.setText(QCoreApplication.translate("loginDialog", u"----", None))
    # retranslateUi

