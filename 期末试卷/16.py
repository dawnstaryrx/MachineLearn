# -*- coding = utf-8 -*-
# @Time : 2022/6/15 14:31
# @Author : 杨荣兴
# @File : 16.py
# @Software : PyCharm
def Traingle(x):
    '''定义杨辉三角的函数，即下一行的第N个元素，是本行的第N个元素和第N-2个元素的和，最后返回一个列表'''
    x = int(x)
    Traingle_list = []
    if x == 1:
        Traingle_list = [1]
    elif x == 2:
        Traingle_list = [1, 1]
    else:
        Traingle_list_temp = Traingle(x - 1)  # 获取上一行三角列表
        Traingle_list = [1, 1]
        temp = 1
        while temp <= x - 2:
            Traingle_list.insert(temp, Traingle_list_temp[temp] + Traingle_list_temp[temp - 1])
            temp += 1

    return Traingle_list


def PrintTringle(x):
    n = 1
    x = int(x)
    # 获取最大的元素，判断列表最大的元素的长度
    if x % 2 == 0:
        max_item = Traingle(x)[int(x / 2)]
    else:
        max_item = Traingle(x)[int((x + 1) / 2)]
    max_length = len(str(max_item))
    while n <= x:
        list = Traingle(n)
        string = ''
        tem = 0
        # 对每一列杨辉三角进行处理，转化成为字符串，拼接
        while tem < len(list):
            if tem == 0:
                string = str(list[tem]).center(max_length)
            else:
                string = string + ' ' + str(list[tem]).center(max_length)
            tem += 1
        # 打印处理，每一列的元素有N个，空格用N+1
        print(string.center((max_length + 1) * x - 1))
        n += 1
PrintTringle(10)