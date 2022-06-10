# -*- coding = utf-8 -*-
# @Time : 2022/6/9 22:12
# @Author : 杨荣兴
# @File : 03.py
# @Software : PyCharm
def word(w=None):
    w[0] = input("1:")
    w[1] = input("2:")
    w[2] = input("3:")
    maxlen = max(len(w[0], w[1], w[2]))
    for i in range(0, maxlen+1):
        