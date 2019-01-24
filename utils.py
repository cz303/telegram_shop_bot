import pymysql


class DB:
    def __init__(self, type="mysql", host=" ", user=" ", password=" ", db=" ", use_cursor=False,
                 ignore_errors=False):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = pymysql.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.connection.commit()
        self.connection.close()
