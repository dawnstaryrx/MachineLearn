# -*- coding = utf-8 -*-
# @Time : 2022/6/10 11:55
# @Author : 杨荣兴
# @File : 12.py
# @Software : PyCharm
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for m in range(1, 6):
                if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
                    print("%d"%(i*1000+j*100+k*10+m))