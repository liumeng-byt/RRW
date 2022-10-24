# -*- coding:utf-8 -*-

def out_color(contant, color=31):
    """
    自定义颜色内容输出到控制台
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    :param contant:
    :param color:
    :return:
    """
    data = "\033[%sm%s\033[0m"%(color,contant)
    return data
