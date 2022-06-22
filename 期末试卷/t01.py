# -*- coding = utf-8 -*-
# @Time : 2022/6/22 9:55
# @Author : 杨荣兴
# @File : t01.py
# @Software : PyCharm
with open("data.txt", 'r') as fp:
    data = fp.readlines()
data = [int(line.strip()) for line in data]
data.sort()
data = [str(i) + "\n" for i in data]
with open("data_asc.txt", 'w') as fp:
    fp.writelines(data)