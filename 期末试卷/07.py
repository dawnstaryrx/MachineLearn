# -*- coding = utf-8 -*-
# @Time : 2022/6/10 10:21
# @Author : 杨荣兴
# @File : 07.py
# @Software : PyCharm

def score(sco):
    if sco < 0 or sco > 100:
        return False
    elif sco >= 90:
        return 'A'
    elif sco >= 80:
        return 'B'
    elif sco >= 70:
        return 'C'
    elif sco >= 60:
        return 'D'
    else:
        return 'E'


sco = float(input("请输入成绩："))
print(score(sco))
