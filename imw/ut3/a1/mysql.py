import pymysql.cursors


class DB():
    def __init__(self, username, password, database):
        self.connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="oscar",
            password="123456",
            db=database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def run(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)

    def query(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
