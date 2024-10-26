import sys
from Login import  LoginDialog
from Profile import MainWindow
from database import DataBase
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)

    data_base = DataBase()

    run = True
    while run:
        login_dialog = LoginDialog(data_base)
        _, login = login_dialog.exec()

        if not login:
            run = False
            break

        profile_window = MainWindow(data_base)
        profile_window.log_in(login)
        profile_window.show()

        a = app.exec()

        login = profile_window.u_id

        if login:
            run = False
            break

    data_base.exit()
