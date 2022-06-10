# -*- coding = utf-8 -*-
# @Time : 2022/6/9 21:00
# @Author : 杨荣兴
# @File : 02.py
# @Software : PyCharm
def divide(n):
    strn = str(n)
    print("千位为：%d" % (int(strn[0])))
    print("百位为：%d" % (int(strn[1])))
    print("十位为：%d" % (int(strn[2])))
    print("个位为：%d" % (int(strn[3])))


num = int(input("请输入一个四位数："))

divide(num)
