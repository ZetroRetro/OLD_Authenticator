from GUI.ui_Login import Ui_loginDialog
from PySide6.QtWidgets import QDialog, QLineEdit
from PySide6.QtCore import Slot
from Register import RegisterDialog


class LoginDialog(QDialog, Ui_loginDialog):
    def __init__(self, data_base=None):
        super().__init__()

        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
        self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.logged_in = False
        self.database = data_base

        self.ui.loginButton.clicked.connect(self.log_in)
        self.ui.showPasswordBox.checkStateChanged.connect(self.password_view)
        self.ui.registerButton.clicked.connect(self.register)

    def set_database(self, data_base):
        self.database = data_base

    @Slot()
    def password_view(self):
        if self.ui.showPasswordBox.isChecked():
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

    @Slot()
    def log_in(self):
        u_id = self.database.login(self.ui.loginEdit.text(),
                                   self.ui.passwordEdit.text())
        if u_id:
            self.logged_in = True
            self.close()
        self.ui.StatusLabel.setText("invalid login/password")

    @Slot()
    def register(self):
        reg_dial = RegisterDialog(data_base=self.database)
        reg_dial.exec()

    def exec(self):
        result = super().exec()
        return result, (self.database.login(self.ui.loginEdit.text(), self.ui.passwordEdit.text())
                        if self.logged_in else '')
