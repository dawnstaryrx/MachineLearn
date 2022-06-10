# -*- coding = utf-8 -*-
# @Time : 2022/6/9 22:21
# @Author : 杨荣兴
# @File : 05.py
# @Software : PyCharm
lis2 = [i for i in range(2, 1000)if 0 not in [i % j for j in range(2, int(i**0.5)+1)]]
print(lis2[-1])
