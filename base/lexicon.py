# coding=utf-8
from abc import abstractmethod

import re
import conf
from util.mysqlUtil import MySQLDB


class Lexicon(object):
    FILE = "LoadInFile"
    DB = "LoadInDB"

    def __init__(self, lexicon=FILE):
        self.model = eval(lexicon + "()")

    def load(self):
        return self.model.load()


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
        result_map = {}
        with open(self.file_name, "r") as file_model:
            for line in file_model:
                entity = LexiconEntity.list_to_obj(re.sub(line, "\s", "").split(","))
                result_map[entity.word] = entity
        return result_map


class LoadInDB(LoadLexicon):
    def __init__(self):
        self.db = MySQLDB(host=conf.lexicon_db_host, user=conf.lexicon_db_user_name, password=conf.lexicon_db_password,
                          database=conf.lexicon_db_database, port=conf.lexicon_db_port)

    def load(self):
        """
        通过数据库加载词典
        :return:
        """
        count = self.get_count()
        t = 10000
        sql = "select word, property from lexicon where status='valid' limit %d," + str(t)
        result_map = {}
        for page in range(count / t if count % t == 0 else (count / t) + 1):
            result_map = dict(LexiconEntity.lists_to_objs(self.db.find(sql, None)), **result_map)
        return result_map

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
