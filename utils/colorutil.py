# -*- coding:utf-8 -*-

def out_color(contant, color=34):
    """
    自定义颜色内容输出到控制台
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    white = 37
    :param contant:
    :param color:
    :return:
    """
    data = "\033[%sm%s\033[0m"%(color,contant)
    return data
