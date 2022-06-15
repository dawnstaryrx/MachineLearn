# -*- coding = utf-8 -*-
# @Time : 2022/6/15 13:45
# @Author : 杨荣兴
# @File : 18.py
# @Software : PyCharm
filename = 'test.txt'
with open(filename, 'w', encoding='UTF-8') as f:
    f.write("莫听穿林打叶声，\n")
    f.write("何妨吟啸且徐行。\n")
    f.write("竹杖芒鞋轻胜马，\n")
    f.write("谁怕？\n")
    f.write("一蓑烟雨任平生。")
    f.close()
with open(filename, 'r', encoding='UTF-8') as f:
    re = f.read()
    print(re)
    f.close()