# -*- coding = utf-8 -*-
# @Time : 2022/6/15 14:11
# @Author : 杨荣兴
# @File : 15.py
# @Software : PyCharm
def get_num():
    x = float(input("请输入一个实数(输入99999终止)："))
    k = [x]
    while abs(x - 99999) > 1e-3:
        x = float(input("请输入一个实数(输入99999终止)："))
        k.append(x)
    k.pop(len(k)-1)
    m = sum(k)/len(k)
    n = []
    for i in range(0, len(k)):
        if k[i] > m:
            n.append(k[i])
    n.append(m)
    n = tuple(n)
    return n


print(get_num())

