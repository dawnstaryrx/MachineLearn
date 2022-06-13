# -*- coding = utf-8 -*-
# @Time : 2022/6/9 22:12
# @Author : 杨荣兴
# @File : 03.py
# @Software : PyCharm
# 编写函数，要求用户从键盘任意输入三个英文单词，按字典顺序输出。
def sor(x, y, z):
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return x, y, z


a, b, c = map(str, input("a b c = ").split())
print(sor(a, b, c))
