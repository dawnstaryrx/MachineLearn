# -*- coding = utf-8 -*-
# @Time : 2022/6/10 11:48
# @Author : 杨荣兴
# @File : 10.py
# @Software : PyCharm
# 99乘法表 左对齐

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d×%d=%d"%(i, j, i*j), end="\t")
    print("\n")