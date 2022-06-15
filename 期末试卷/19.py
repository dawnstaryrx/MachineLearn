# -*- coding = utf-8 -*-
# @Time : 2022/6/15 13:43
# @Author : 杨荣兴
# @File : 19.py
# @Software : PyCharm
filename = 'demo6.py'
with open(filename, 'r', encoding="utf-8") as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))

lines = [line.rstrip().ljust(maxLength) + '#' + str(index) + '\n'
         for index, line in enumerate(lines)]

with open(filename[:-3]+'_new.py', 'w', encoding="utf-8") as fp:
    fp.writelines(lines)
