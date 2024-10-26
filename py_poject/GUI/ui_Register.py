# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterEcEunO.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_registrationDialog(object):
    def setupUi(self, RegistrationDialog):
        if not RegistrationDialog.objectName():
            RegistrationDialog.setObjectName(u"RegistrationDialog")
        RegistrationDialog.resize(492, 442)
        self.verticalLayout_3 = QVBoxLayout(RegistrationDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLabel = QLabel(RegistrationDialog)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.verticalLayout.addWidget(self.usernameLabel)

        self.usernameEdit = QLineEdit(RegistrationDialog)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.verticalLayout.addWidget(self.usernameEdit)

        self.emailLabel = QLabel(RegistrationDialog)
        self.emailLabel.setObjectName(u"emailLabel")

        self.verticalLayout.addWidget(self.emailLabel)

        self.emailEdit = QLineEdit(RegistrationDialog)
        self.emailEdit.setObjectName(u"emailEdit")

        self.verticalLayout.addWidget(self.emailEdit)

        self.nameLabel = QLabel(RegistrationDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.verticalLayout.addWidget(self.nameLabel)

        self.nameEdit = QLineEdit(RegistrationDialog)
        self.nameEdit.setObjectName(u"nameEdit")

        self.verticalLayout.addWidget(self.nameEdit)

        self.ageLabel = QLabel(RegistrationDialog)
        self.ageLabel.setObjectName(u"ageLabel")

        self.verticalLayout.addWidget(self.ageLabel)

        self.ageEdit = QLineEdit(RegistrationDialog)
        self.ageEdit.setObjectName(u"ageEdit")

        self.verticalLayout.addWidget(self.ageEdit)

        self.sexLabel = QLabel(RegistrationDialog)
        self.sexLabel.setObjectName(u"sexLabel")

        self.verticalLayout.addWidget(self.sexLabel)

        self.sexEdit = QLineEdit(RegistrationDialog)
        self.sexEdit.setObjectName(u"sexEdit")

        self.verticalLayout.addWidget(self.sexEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.passwordLabel1 = QLabel(RegistrationDialog)
        self.passwordLabel1.setObjectName(u"passwordLabel1")

        self.verticalLayout.addWidget(self.passwordLabel1)

        self.passwordEdit1 = QLineEdit(RegistrationDialog)
        self.passwordEdit1.setObjectName(u"passwordEdit1")

        self.verticalLayout.addWidget(self.passwordEdit1)

        self.passwordLabel2 = QLabel(RegistrationDialog)
        self.passwordLabel2.setObjectName(u"passwordLabel2")

        self.verticalLayout.addWidget(self.passwordLabel2)

        self.passwordEdit2 = QLineEdit(RegistrationDialog)
        self.passwordEdit2.setObjectName(u"passwordEdit2")

        self.verticalLayout.addWidget(self.passwordEdit2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.statusLabel = QLabel(RegistrationDialog)
        self.statusLabel.setObjectName(u"statusLabel")

        self.verticalLayout.addWidget(self.statusLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.saveButton = QPushButton(RegistrationDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout_2.addWidget(self.saveButton)

        self.cancelButton = QPushButton(RegistrationDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_2.addWidget(self.cancelButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(RegistrationDialog)

        QMetaObject.connectSlotsByName(RegistrationDialog)
    # setupUi

    def retranslateUi(self, RegistrationDialog):
        RegistrationDialog.setWindowTitle(QCoreApplication.translate("RegistrationDialog", u"Registration", None))
        self.usernameLabel.setText(QCoreApplication.translate("RegistrationDialog", u"Username:", None))
        self.emailLabel.setText(QCoreApplication.translate("RegistrationDialog", u"Email:", None))
        self.nameLabel.setText(QCoreApplication.translate("RegistrationDialog", u"Name:", None))
        self.ageLabel.setText(QCoreApplication.translate("RegistrationDialog", u"Age:", None))
        self.sexLabel.setText(QCoreApplication.translate("RegistrationDialog", u"Sex:", None))
        self.passwordLabel1.setText(QCoreApplication.translate("RegistrationDialog", u"Password:", None))
        self.passwordLabel2.setText(QCoreApplication.translate("RegistrationDialog", u"Repeat Password", None))
        self.statusLabel.setText(QCoreApplication.translate("RegistrationDialog", u"----", None))
        self.saveButton.setText(QCoreApplication.translate("RegistrationDialog", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("RegistrationDialog", u"Cancel", None))
    # retranslateUi

