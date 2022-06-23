# -*- coding = utf-8 -*-
# @Time : 2022/6/23 9:04
# @Author : 杨荣兴
# @File : AdaBoost.py
# @Software : PyCharm
import math
D1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
y1 = [1, 1, 1, -1, -1, -1, -1, 1, 1, -1]
G1 = [1, 1, 1, -1, -1, -1, -1, -1, -1, -1]
# 误差率
e1 = 0.2
# 系数
a1 = (1/2) * math.log((1 - e1)/e1, math.e)
print("系数a为：", a1)
z1 = 2 * math.sqrt(e1 * (1 - e1))
print("z1 = ", z1)
D2 = []
for i in range(0, len(D1)):
    D2.append((D1[i]/z1) * math.exp(-a1*y1[i]*G1[i]))
print("D2 = ", D2)
