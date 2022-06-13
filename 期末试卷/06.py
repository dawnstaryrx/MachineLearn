# -*- coding = utf-8 -*-
# @Time : 2022/6/13 16:01
# @Author : 杨荣兴
# @File : 06.py
# @Software : PyCharm
import random
import string
x = string.ascii_letters + string.digits + string.punctuation
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
d = dict()
for ch in z:
    d[ch] = d.get(ch, 0) + 1  # 函数返回指定键的值
print(d)