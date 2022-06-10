# -*- coding = utf-8 -*-
# @Time : 2022/6/10 15:27
# @Author : 杨荣兴
# @File : 20.py
# @Software : PyCharm
while True:
    x = input("请输入一个数字字符串：")
    try :
        x = int(x)
        print("你要输入的字符串是：%d" %x)
        break
    except Exception as e:
        print("产生异常！")