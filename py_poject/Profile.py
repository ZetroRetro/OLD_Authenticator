from GUI.ui_Profile import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self, data_base=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.u_id = ''
        self.database = data_base

        self.ui.signOutButton.clicked.connect(self.log_out)
        self.ui.discardButton.clicked.connect(self.load_data)
        self.ui.saveButton.clicked.connect(self.save_data)

        self.ui.nameEdit.textChanged.connect(self.enable_save)
        self.ui.ageEdit.textChanged.connect(self.enable_save)
        self.ui.sexEdit.textChanged.connect(self.enable_save)

    def set_database(self, data_base):
        self.database = data_base

    def log_in(self, login):
        if not login:
            raise ValueError("Unable to log in with null-identificatior")
        self.u_id = login

        self.load_data()

    @Slot()
    def log_out(self):
        self.u_id = ''
        self.close()

    @Slot()
    def load_data(self):
        data = (self.database.get_user(self.u_id), self.database.load_data(self.u_id))
        if len(data[0]) == 0:
            raise ValueError("Unable to load login/mail")
        if len(data[1]) == 0:
            raise ValueError("Unable to load user data")

        user_log = data[0][0]
        user_data = data[1][0]

        self.ui.usernameLabel.setText(user_log[0])
        self.ui.userEmailLabel.setText(user_log[1])

        self.ui.nameEdit.setText(str(user_data[1]))
        self.ui.ageEdit.setText(str(user_data[2]))
        self.ui.sexEdit.setText(str(user_data[3]))

        self.ui.saveButton.setEnabled(False)

    @Slot()
    def save_data(self):
        complains = self.database.check_format(name=self.ui.nameEdit.text(),
                                               age=self.ui.ageEdit.text(),
                                               sex=self.ui.sexEdit.text())

        if complains != "":
            self.statusBar().showMessage(complains)
            return

        self.database.update_data(self.u_id, (self.ui.nameEdit.text(),
                                              int(self.ui.ageEdit.text()),
                                              self.ui.sexEdit.text()))
        self.load_data()

    def enable_save(self):
        self.ui.saveButton.setEnabled(True)