from GUI.ui_Register import Ui_registrationDialog
from PySide6.QtWidgets import QDialog, QLineEdit
from PySide6.QtCore import Slot


class RegisterDialog(QDialog):
    def __init__(self, data_base=None):
        super().__init__()

        self.ui = Ui_registrationDialog()
        self.ui.setupUi(self)
        self.ui.passwordEdit1.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.passwordEdit2.setEchoMode(QLineEdit.EchoMode.Password)

        self.database = data_base

        self.ui.saveButton.clicked.connect(self.create_account)
        self.ui.cancelButton.clicked.connect(self.close)

    def load_database(self, data_base):
        self.database = data_base

    @Slot()
    def create_account(self):
        complains = self.database.check_format(usrnm=self.ui.usernameEdit.text(),
                                               mail=self.ui.emailEdit.text(),
                                               pswrd1=self.ui.passwordEdit1.text(),
                                               pswrd2=self.ui.passwordEdit2.text(),
                                               name=self.ui.nameEdit.text(),
                                               age=self.ui.ageEdit.text(),
                                               sex=self.ui.sexEdit.text())
        if complains != "":
            self.ui.statusLabel.setText(complains)
            return
        self.ui.statusLabel.setText("Success")

        self.database.register([[self.ui.usernameEdit.text(), self.ui.emailEdit.text(), self.ui.passwordEdit1.text()],
                                [self.ui.nameEdit.text(), self.ui.ageEdit.text(), self.ui.sexEdit.text()]])

        self.close()

