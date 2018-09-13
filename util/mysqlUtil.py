# coding=utf-8
import pymysql

import conf

"""
    mysql  connection  class
"""


class MySQLDB(object):
    def __init__(self, host, user, password, database, port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.connect = MySQLDB.init(host, user, password, database, port, charset)

    @staticmethod
    def init(host, user, password, database, port, charset):
        """
        create mysql connect
        :param host:
        :param user:
        :param password:
        :param database:
        :param port:
        :param charset:
        :return:
        """
        return pymysql.connect(host=host, user=user, password=password, port=port, database=database, charset=charset)

    @staticmethod
    def execute(sql, args, connect):
        """
        执行sql语句 返回结果 自动提交事务
        :param sql:         sql语句
        :param args:        sql参数
        :param connect:     数据库连接
        :return:
        """
        with connect.cursor() as cursor:
            result = cursor.execute(sql, args)
            connect.commit()
        return result

    @staticmethod
    def query(sql, args, connect):
        """
        执行sql语句 返回结果
        :param sql:         sql语句
        :param args:        sql参数
        :param connect:     数据库连接
        :return:
        """
        with connect.cursor() as cursor:
            cursor.execute(sql, args)
            result = cursor.fetchall()
        return result

    def find(self, sql, args):
        """
        执行查询语句 返回结果
        :param sql:
        :param args:
        :return:
        """
        return MySQLDB.query(sql, args, self.connect)

    def execute_sql(self, sql, args):
        """
        执行sql语句 返回结果
        :param sql:
        :param args:
        :return:
        """
        return MySQLDB.execute(sql, args, self.connect)

    def count(self, sql, args):
        """
        执行sql语句 返回单个结果
        :param sql:
        :param args:
        :return:
        """
        return self.find(sql, args)[0][0]


if __name__ == "__main__":
    db = MySQLDB(host=conf.lexicon_db_host, user=conf.lexicon_db_user_name, password=conf.lexicon_db_password,
                 database=conf.lexicon_db_database, port=conf.lexicon_db_port)
    for a in db.find("select * from lexicon", None)[0]:
        print a
