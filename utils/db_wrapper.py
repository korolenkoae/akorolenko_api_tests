import mysql.connector

# https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor


class DbWrapper:
    cursor: MySQLCursor
    connection: MySQLConnection

    def __init__(self, host, user, password, database, passphrase=None, ssh_user=None):
        """
        Метод инициализации работы с БД
        :param host: Адрес хоста БД
        :param user: Имя пользователя БД
        :param password: Пароль пользлователя БД
        :param database: Название БД
        :param passphrase: Пароль для SSH ключа
        :param ssh_user: Имя пользователя SSH туннеля
        """
        if passphrase is None and ssh_user is None:
            self.connection = mysql.connector.connect(host=host, user=user, passwd=password, database=database)
        self.cursor = self.connection.cursor()
        self.cursor_buffered = self.connection.cursor(buffered=True)

    def query(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor

    def insertmany(self, sql, args):
        self.cursor.executemany(sql, args)
        rowcount = self.cursor.rowcount
        self.connection.commit()
        return rowcount

    def update(self, sql, args):
        cursor = self.query(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        return rowcount

    def fetch(self, sql, args):
        rows = []
        cursor = self.query(sql, args)
        if cursor.with_rows:
            rows = cursor.fetchall()
        return rows

    def fetchone(self, sql, args):
        row = None
        cursor = self.query(sql, args)
        if cursor.with_rows:
            row = cursor.fetchone()
        return row

    def __del__(self):
        if self.cursor:
            try:
                self.cursor.close()
            except Exception:
                pass
        if self.cursor_buffered:
            try:
                self.cursor_buffered.close()
            except Exception:
                pass
        if self.connection:
            try:
                self.connection.close()
            except Exception:
                pass
