# coding=utf-8
from abc import abstractmethod


class BaseRobot(object):
    @abstractmethod
    def dispose(self, data):
        pass
