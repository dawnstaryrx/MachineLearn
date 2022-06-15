# -*- coding = utf-8 -*-
# @Time : 2022/6/15 13:31
# @Author : 杨荣兴
# @File : 11.py
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


i = int(input("输入整数："))
print("%d是不是素数？"%i)
if issushu(i):
    print("是")
else:
    print("不是")
