# coding=utf-8

import re


def wipe_repetition(str_data, str_max=800):
    """
    去除连续的重复字符串
    :param str_data:    待处理字符串
    :param str_max:     待处理字符串最大长度 默认800
    :return:
    """
    if not str_data:
        return ""
    str_data = str_data.strip()
    if len(str_data) > str_max:
        raise Exception("input data must less then str_max")
    # 转换为字符串数组
    str_list = list(unicode(str_data, "utf-8"))
    current = ""
    remove = []
    # 如果与上一个字符串相同 则放入删除数组中，正序放入数组， 按数组删除时使用倒序
    for i, element in enumerate(str_list):
        if element == current:
            remove.append(i)
        current = element
    for i in reversed(remove):
        str_list.pop(i)
    return "".join(str_list)


if __name__ == "__main__":
    print wipe_repetition("一闪一闪亮晶晶 满天都是小星星 挂在天上放光明 好像,,,,,一颗大眼睛")
    print wipe_repetition("慌慌张张 匆匆忙忙 为何生活总是这样 难道说 我的理想 就是..32.3这样度过一生的时光")
