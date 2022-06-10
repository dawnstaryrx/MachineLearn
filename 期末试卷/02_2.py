# -*- coding = utf-8 -*-
# @Time : 2022/6/9 22:00
# @Author : 杨荣兴
# @File : 02_2.py
# @Software : PyCharm
def divide(n):
    num = []
    num.append(n // 1000 % 10)
    num.append(n // 100 % 10)
    num.append((n // 10 % 10))
    num.append(n % 10)
    return num


num = 1234
print(divide(num))
