# -*- coding = utf-8 -*-
# @Time : 2022/6/13 15:08
# @Author : 杨荣兴
# @File : 04.py
# @Software : PyCharm
# 4 编写程序，把列表x = [a,b,a,b,a,b,a,b,a,b,a,b,a]中的所有a删掉。
x = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a']
l = len(x) - 1
while l >= 0:
    if x[l] == 'a':
        x.pop(l)
    l -= 1
print(x)
