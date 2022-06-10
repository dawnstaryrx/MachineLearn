# -*- coding = utf-8 -*-
# @Time : 2022/6/10 10:26
# @Author : 杨荣兴
# @File : 09.py
# @Software : PyCharm
# 今天是今年的第几天

def run_year(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False


def date(y, m, d):
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ssum = 0
    if run_year(y):
        for i in range(0, m):
            ssum = ssum + month[i]
        ssum = ssum + d
        if m > 2:
            ssum = ssum + 1
    else:
        for i in range(0, m):
            ssum = ssum + month[i]
        ssum = ssum + d
    return ssum


try:
    y = int(input("请输入年："))
    m = int(input("请输入月："))
    d = int(input("请输入日："))
except:
    print("输入错误！")

print("是第%d天" % date(y, m, d))
