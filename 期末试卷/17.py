# -*- coding = utf-8 -*-
# @Time : 2022/6/15 13:57
# @Author : 杨荣兴
# @File : 17.py
# @Software : PyCharm
def issushu(n):
    if n == 1:
        return False
    if n == 2:
        return True
    issu = True
    for i in range(2, n):
        if n%i == 0:
            issu = False
    if issu == True:
        return True
    else:
        return False

while True:
    a = int(input("输入一个偶数："))
    if a % 2 == 1:
        print("输入有误，请重新输入！")
        continue
    else:
        break

su = []
for i in range(1, 1000):
    if issushu(i):
        su.append(i)

for i in range(0, len(su)):
    for j in range(0, len(su)):
        if su[i] + su[j] == a:
            print("%d + %d = %d" % (su[i], su[j], a))
