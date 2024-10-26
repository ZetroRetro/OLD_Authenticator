import sqlite3
import hashlib
import os
import re

class DataBase:
    CREATE_DATABASE: str = """
        CREATE TABLE user_password (
            login text,
            mail text,
            password text,
            id text);
        CREATE TABLE user_data (
            id text,
            name text,
            age integer,
            sex text);
    """
    GET_USER_MAIL: str = """
        SELECT login, mail FROM user_password WHERE
        id = '{u_id}';
    """

    GET_USER_WITH_LOGIN: str = """
        SELECT login, mail FROM user_password WHERE
        login = '{login}' OR mail = '{login}';
    """

    GET_USER_ID: str = """
        SELECT id FROM user_password WHERE 
        (login = '{login}' OR mail = '{login}') AND password = '{password}';
    """
    GET_USER_DATA: str = """
        SELECT * FROM user_data WHERE
        id = '{u_id}';
    """
    ADD_USER: str = """
        INSERT INTO user_password VALUES ('{login}', '{mail}', '{password}', '{u_id}');
    """
    ADD_USER_DATA: str = """
        INSERT INTO user_data VALUES {data};
    """
    UPDATE_DATA: str = """
        UPDATE user_data SET
            name = '{name}', 
            age = {age}, 
            sex = '{sex}' 
        WHERE
            id = '{u_id}';
    """

    def __init__(self, path='./UserData.db'):
        if not self.check_path(path):
            raise ConnectionError("Incorrect File Path")
        if not self.check_for_db(path):
            data_base = sqlite3.connect(path)
            cursor = data_base.cursor()
            cursor.executescript(self.CREATE_DATABASE)
            data_base.commit()
            data_base.close()
            del data_base, cursor

        self.data_base = sqlite3.connect(path)
        self.cursor = self.data_base.cursor()

    @staticmethod
    def check_path(path: str) -> bool:
        return os.path.exists('/'.join(path.split("/")[:-1]) + '/')

    @staticmethod
    def check_for_db(path: str) -> bool:
        return os.path.exists(path) and os.path.isfile(path)

    @staticmethod
    def __encrypt__(data: str):
        return hashlib.sha512(data.encode()).hexdigest()

    # returns user id if login/password are valid
    def login(self, user: str, password: str) -> str:
        self.cursor.execute(self.GET_USER_ID.format(login=user, password=password))
        user_id = self.cursor.fetchall()

        if not user_id:
            return ''  # returns no user
        return user_id[0][0]

    def get_username_mail(self, login: str):
        self.cursor.execute(self.GET_USER_WITH_LOGIN.format(login=login))
        return self.cursor.fetchall()

    def load_data(self, u_id: str):
        self.cursor.execute(self.GET_USER_DATA.format(u_id=u_id))
        user_data = self.cursor.fetchall()

        return user_data

    def get_user(self, u_id):
        self.cursor.execute(self.GET_USER_MAIL.format(u_id=u_id))
        return self.cursor.fetchall()

    def register(self, data) -> None:
        if not len(data) == 2:
            raise ValueError("User data list must include 2 sublists")
        if not len(data[0]) == 3:
            raise ValueError("User login data must include: login, mail and password")

        user_log: list = data[0]
        user_data: list = [self.__encrypt__(user_log[0])] + data[1]

        self.cursor.executescript(self.ADD_USER.format(login=user_log[0], mail=user_log[1],
                                                 password=user_log[2], u_id=self.__encrypt__(user_log[0])))
        print(user_data)
        self.cursor.executescript(self.ADD_USER_DATA.format(data=tuple(user_data)))

        self.data_base.commit()

    def update_data(self, u_id, data):
        self.cursor.executescript(self.UPDATE_DATA.format(name=data[0], age=int(data[1]),
                                                          sex=data[2], u_id=u_id))
        self.data_base.commit()

    def exit(self):
        self.data_base.close()

    def check_format(self, usrnm="...", mail="...", pswrd1="...", pswrd2="...", name="...", age="0", sex="..."):
        if usrnm != "...":
            cmpl = self.check_username(usrnm)
            if cmpl != "":
                return cmpl

        if mail != "...":
            cmpl = self.check_email(mail)
            if cmpl != "":
                return cmpl

        if pswrd1 != "...":
            cmpl = self.check_password(pswrd1, pswrd2)
            if cmpl != "":
                return cmpl

        if name != "...":
            cmpl = self.check_name(name)
            if cmpl != "":
                return cmpl

        if age != "...":
            cmpl = self.check_age(age)
            if cmpl != "":
                return cmpl

        if sex != "...":
            cmpl = self.check_sex(sex)
            if cmpl != "":
                return cmpl
        return ""

    def check_username(self, username: str) -> str:
        if not re.match(r"[a-zA-Z_][a-zA-Z0-9_\-.]*", username):
            return "Username must only include letters, digits and special symbols: ('.', '-', '_')"
        if len(self.get_username_mail(username)) != 0:
            return "User with such login already exists"
        return ""

    def check_email(self, mail: str) -> str:
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mail):
            return "Wrong email format"
        if len(self.get_username_mail(mail)) != 0:
            return "User with such mail already exists"
        return ""

    def check_password(self, password1: str, password2: str="...") -> str:
        if password2 == '...':
            password2 = password1

        if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password1):
            return ("Password must have at least 8 symbols that must be restricted to: " + '\n'
                    "letters (a-z and A-Z), digits (0-9) and special symbols (@#$%^&+=)")
        if password1 != password2:
            return "Passwords don't match"
        return ""

    def check_name(self, name: str):
        return ""

    def check_age(self, age: str) -> str:
        if not re.match(r"[1-9][0-9]*",age):
            return "Age must be a number > 0"
        return ""

    def check_sex(self, sex: str):
        return ""

'''
def create_db(c):
    c.execute("""CREATE TABLE articles (
        title text,
        full_text text,
        views integer,
        avtor text
        )
    """)


def add_data_in_db(c):
    c.executescript("""
    INSERT INTO user_password VALUES ('Admin', 'example@try.com', '1234567890', '0');
    INSERT INTO user_data     VALUES ('0', 'Иванов_Иван', 101, 'male');
    """)

def add_data_in_db_2(c):
    c.execute("""
        INSERT INTO user_password VALUES ('test', 'test@test.test', 'test', 'test')""")
    c.execute("""
        INSERT INTO user_data     VALUES ('test', 'test', 7357, 'test');""")


def data_selection(c):
    c.execute("""SELECT * FROM articles""")
    print(c.fetchall())
    c.execute("""SELECT rowid, title FROM articles""")
    print(c.fetchall())
    c.execute("""SELECT avtor, title FROM articles""")
    print(c.fetchmany(1))
    print(c.fetchone())


def data_cycling(c):
    c.execute("""SELECT rowid, * FROM articles""")
    items = c.fetchall()

    for el in items:
        print(el[1] + "\n" + el[4] + "\n")

def data_filtering(c):
    c.execute("""SELECT rowid, * FROM articles WHERE rowid <= 2""")
    items = c.fetchall()
    print(*items, sep='\n', end='\n\n')

    c.execute("""SELECT rowid, * FROM articles WHERE views >= 60""")
    items = c.fetchall()
    print(*items, sep='\n', end='\n\n')

    c.execute("""SELECT rowid, * FROM articles WHERE views >= 60 ORDER BY rowid DESC""")
    items = c.fetchall()
    print(*items, sep='\n', end='\n\n')

def data_delete(c):
    c.execute("""DELETE FROM articles WHERE rowid = 2""")
'''