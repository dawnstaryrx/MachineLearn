# -*- coding = utf-8 -*-
# @Time : 2022/6/10 12:41
# @Author : 杨荣兴
# @File : 13.py
# @Software : PyCharm
# 编写程序，生成一个含有20个随机整数的列表，要求所有元素不相同，并且每个元素的值介于1到100之间。
import random


def check(lst):
    set_list = set(lst)
    if len(set_list) == len(lst):
        return False
    else:
        return True


n = []
for i in range(0, 20):
    num = random.randint(1, 100)
    n.append(num)
    while check(n):
        n[i] = random.randint(1, 100)

print(n)
