# -*- coding = utf-8 -*-
# @Time : 2022/6/15 13:25
# @Author : 杨荣兴
# @File : 08.py
# @Software : PyCharm

def score():
    sco = []
    jus = 'yes'
    num = 0
    while jus == 'yes':
        sco.append(int(input("输入成绩：")))
        num += 1
        jus = input("是否继续输入：(yes/no)")
    print("平均成绩为：%.2f" % (sum(sco) / num))


score()
