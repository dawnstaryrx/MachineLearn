# -*- coding = utf-8 -*-
# @Time : 2022/6/13 14:57
# @Author : 杨荣兴
# @File : 00.py
# @Software : PyCharm
import os
x = [filename for filename in os.listdir('.') if filename.endswith('.py')]
print(x)