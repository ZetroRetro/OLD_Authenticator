# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfileizgHzv.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(452, 285)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.WelcomeLabel = QLabel(self.centralwidget)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.WelcomeLabel.setFont(font)

        self.horizontalLayout.addWidget(self.WelcomeLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.GridLayout = QGridLayout()
        self.GridLayout.setObjectName(u"GridLayout")
        self.GridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.usernameLabel = QLabel(self.centralwidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.GridLayout.addWidget(self.usernameLabel, 0, 1, 1, 1)

        self.userEmailLabel = QLabel(self.centralwidget)
        self.userEmailLabel.setObjectName(u"userEmailLabel")

        self.GridLayout.addWidget(self.userEmailLabel, 1, 1, 1, 1)

        self.emailLabel = QLabel(self.centralwidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.GridLayout.addWidget(self.emailLabel, 1, 0, 1, 1)

        self.userLabel = QLabel(self.centralwidget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setLayoutDirection(Qt.LeftToRight)
        self.userLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.GridLayout.addWidget(self.userLabel, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.GridLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.signOutButton = QPushButton(self.centralwidget)
        self.signOutButton.setObjectName(u"signOutButton")
        self.signOutButton.setMouseTracking(False)
        self.signOutButton.setTabletTracking(False)
        self.signOutButton.setStyleSheet(u"color: rgb(158, 20, 20);\n"
"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.signOutButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.verticalLayout.addWidget(self.nameLabel)

        self.nameEdit = QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.verticalLayout.addWidget(self.nameEdit)

        self.ageLabel = QLabel(self.centralwidget)
        self.ageLabel.setObjectName(u"ageLabel")

        self.verticalLayout.addWidget(self.ageLabel)

        self.ageEdit = QLineEdit(self.centralwidget)
        self.ageEdit.setObjectName(u"ageEdit")

        self.verticalLayout.addWidget(self.ageEdit)

        self.sexLabel = QLabel(self.centralwidget)
        self.sexLabel.setObjectName(u"sexLabel")

        self.verticalLayout.addWidget(self.sexLabel)

        self.sexEdit = QLineEdit(self.centralwidget)
        self.sexEdit.setObjectName(u"sexEdit")

        self.verticalLayout.addWidget(self.sexEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout_2.addWidget(self.saveButton)

        self.discardButton = QPushButton(self.centralwidget)
        self.discardButton.setObjectName(u"discardButton")

        self.verticalLayout_2.addWidget(self.discardButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.WelcomeLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome to your profile", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"{user_name}", None))
        self.userEmailLabel.setText(QCoreApplication.translate("MainWindow", u"{user_email}", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"email:", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"user:", None))
        self.signOutButton.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.ageLabel.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.sexLabel.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.discardButton.setText(QCoreApplication.translate("MainWindow", u"Discard Changes", None))
    # retranslateUi

