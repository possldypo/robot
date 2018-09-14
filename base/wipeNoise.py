# encoding=utf-8
"""
文本去噪
"""
from util.regex import wipe_repetition


class WipeNoise(object):
    @staticmethod
    def wipe_noise(str_data):
        return wipe_repetition(str_data)
