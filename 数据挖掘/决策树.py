# -*- coding = utf-8 -*-
# @Time : 2022/6/21 15:33
# @Author : 杨荣兴
# @File : 决策树.py
# @Software : PyCharm
import math
# 如果可以用python计算的话
t = [2, 1]  # 修改t， 6，4为正负样本的个数
IT = 0
GiniT = 1
for i in t:
    IT -= i/sum(t)*math.log2(i/sum(t))
    GiniT -= pow(i/sum(t), 2)
print("信息熵I(T)=%.4f" % IT)
print("基尼指数Gini(T)=%.4f" % GiniT)
