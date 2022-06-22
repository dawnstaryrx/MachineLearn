# -*- coding = utf-8 -*-
# @Time : 2022/6/22 8:18
# @Author : 杨荣兴
# @File : K均值.py
# @Software : PyCharm
def ou_long(a, b):
    d = pow(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2), 1 / 2)
    return d


u1 = [2.5, 2]  # u1 u2是均值向量
u2 = [2, 0]  # 需要自己修改
x = [[0, 2], [0, 0], [1, 0], [5, 0], [5, 2]]
print("初始均值向量为u1 = (%.2f, %.2f), u2 = (%.2f, %.2f)" % (u1[0], u1[1], u2[0], u2[1]))
for i in range(1, len(x) + 1):
    print("x%d 到 u1 的长度 = %.2f    x%d 到 u2 的长度 = %.2f" % (i, ou_long(x[i - 1], u1), i, ou_long(x[i - 1], u2)))
    if ou_long(x[i - 1], u1) < ou_long(x[i - 1], u2):
        print("x%d 应被划入 c1" % i)
    else:
        print("x%d 应被划入 c2" % i)
