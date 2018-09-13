# coding=utf-8
from abc import abstractmethod

import conf
from util.mysqlUtil import MySQLDB


class Lexicon(object):
    FILE = "file"
    DB = "db"

    def __init__(self, lexicon=FILE):
        pass

    def load_file(self):
        pass

    def load_db(self):
        pass


class LoadLexicon(object):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load(self):
        pass


class LoadInFile(LoadLexicon):
    def __init__(self):
        self.file_name = conf.lexicon_file_path

    def load(self):
        pass


class LoadInDB(LoadLexicon):
    def __init__(self):
        self.db = MySQLDB(host=conf.lexicon_db_host, user=conf.lexicon_db_user_name, password=conf.lexicon_db_password,
                          database=conf.lexicon_db_database, port=conf.lexicon_db_port)

    def load(self):
        pass

    def get_count(self):
        """
        获取词典总数
        :return:
        """
        sql = "select count(1) from lexicon"
        return self.db.count(sql, None)


class LexiconEntity(object):
    # 词语
    word = None
    # 词性
    property = None

    def __init__(self, word, property):
        self.word = word
        self.property = property

    @staticmethod
    def list_to_obj(list_data):
        """
        将数组转为对象
        :param list_data:
        :return:
        """
        return LexiconEntity(list_data[0], list_data[1])

    @staticmethod
    def lists_to_objs(list_datas):
        """
        将二维数组转为多个对象
        :param list_datas:
        :return: 对象字典
        """
        return {list_data[0]: LexiconEntity.list_to_obj(list_data) for list_data in list_datas}
