# coding=utf-8
from abc import abstractmethod


class BaseDB(object):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def remove(self, query):
        pass

    @abstractmethod
    def update(self, query, data):
        pass

    @abstractmethod
    def query(self, query, limit, skip):
        pass

