# 一.（每小题5分,共20分）

> 1 请谈谈你对Python语言的认识？

1. Python是一种解释型语言，这意味着在开发过程中没有了编译这个环节。
2. Python是一种交互式语言。
3. Python是面向对象的语言，支持面向对象的风格或代码封装在对象的编程技术。
4. Python是开源的，拥有很庞大的社区。
5. Python是一种动态语言，变量类型可以随时变化。

> 2 编写函数，要求用户输入一个四位自然数，计算并输出其千位、佰位、 十位和个位上的数字。  

数字转为字符串，字符串再转为数字。

```python
def divide(n):
    strn = str(n)
    print("千位为：%d" % (int(strn[0])))
    print("百位为：%d" % (int(strn[1])))
    print("十位为：%d" % (int(strn[2])))
    print("个位为：%d" % (int(strn[3])))


num = int(input("请输入一个四位数："))

divide(num)
```

整除取余。

```python
def divide(n):
    num = []
    num.append(n // 1000 % 10)
    num.append(n // 100 % 10)
    num.append((n // 10 % 10))
    num.append(n % 10)
    return num


num = 1234
print(divide(num))
```

> 3 编写函数，要求用户从键盘任意输入三个英文单词，按字典顺序输出。  

```python
def sor(x, y, z):
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return x, y, z


a, b, c = map(str, input("a b c = ").split())
print(sor(a, b, c))
```

> 4 编写程序，把列表x = [a,b,a,b,a,b,a,b,a,b,a,b,a]中的所有a删掉。  

```python
x = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a']
l = len(x) - 1
while l >= 0:
    if x[l] == 'a':
        x.pop(l)
    l -= 1
print(x)
```

# 二．（每小题 5分，共20分）
　　　
> 5．使用列表推导式生成1000以内的最大的素数。  

```python
lis2 = [i for i in range(2, 1000)if 0 not in [i % j for j in range(2, int(i**0.5)+1)]]
print(lis2[-1])
```

> 6 编写函数，首先生成包含1000个随机字符的字符串，然后统计每个字符的出现次数。  

```python
import random
import string
x = string.ascii_letters + string.digits + string.punctuation
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
d = dict()
for ch in z:
    d[ch] = d.get(ch, 0) + 1  # 函数返回指定键的值
print(d)
```

> 7 编写函数，要求利用多分支选择结构将成绩从百分制变换到等级制。（注意：等级分ABCDE五个等级）  

```python
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

```

>8 编写函数，用户输入若干个分数，求所有分数的平均分。每输入一个分数
后询问是否继续输入下一个分数，回答“yes”就继续输入下一个分数，回答
“no”就停止输入分数。

```python
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
```

# 三.（每小题4分，共20分）                

> 9.编写函数，判断今天是今年的第几天？

```python
# -*- coding = utf-8 -*-
# @Time : 2022/6/10 10:26
# @Author : 杨荣兴
# @File : 09.py
# @Software : PyCharm
# 今天是今年的第几天

def run_year(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False


def date(y, m, d):
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ssum = 0
    if run_year(y):
        for i in range(0, m):
            ssum = ssum + month[i]
        ssum = ssum + d
        if m > 2:
            ssum = ssum + 1
    else:
        for i in range(0, m):
            ssum = ssum + month[i]
        ssum = ssum + d
    return ssum


try:
    y = int(input("请输入年："))
    m = int(input("请输入月："))
    d = int(input("请输入日："))
except:
    print("输入错误！")

print("是第%d天" % date(y, m, d))

```

```text
判断闰年的简单办法：
import calendar
calendar.isleap(2022) # False
calendar.isleap(2020) # True
计算两个日期之间相差多少天：
def dayBetween(y1, m1, d1, y2, m2, d2):
    from datetime import date
    dif = date(y1, m1, d1)
    dif = dif - date(y2, m2, d2)
    return dif.days
```

> 10 打印九九乘法表。要求：左对齐。

```python
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d×%d=%d"%(i, j, i*j), end="\t")
    print("\n")
```

> 11 编写函数，要求输入一个数，判断一个这个数是否为素数。

```python
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
```

> 12 编写程序，输出由1、2、3、4、5这五个数字组成的每位数都不相同的所有四位数。

```python
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for m in range(1, 6):
                if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
                    print("%d"%(i*1000+j*100+k*10+m))
```

# 四．（每小题4分，共20分）

> 13．编写程序，生成一个含有20个随机整数的列表，要求所有元素不相同，并且每个元素的值介于1到100之间。

```python
# -*- coding = utf-8 -*-
# @Time : 2022/6/10 12:41
# @Author : 杨荣兴
# @File : 13.py
# @Software : PyCharm
# 编写程序，生成一个含有20个随机整数的列表，要求所有元素不相同，并且每个元素的值介于1到100之间。
import random


def check(lst):
    set_list = set(lst)
    if len(set_list) == len(lst):
        return False
    else:
        return True


n = []
for i in range(0, 20):
    num = random.randint(1, 100)
    n.append(num)
    while check(n):
        n[i] = random.randint(1, 100)

print(n)
```

> 14．凯撒加密，每个字母替换为后面第k个。（注意：小写字母循环小写字母，
大写字母循环大写字母）。

```python
import string


def kaisa(s, k):
    lower = string.ascii_lowercase  # 小写字母
    upper = string.ascii_uppercase  # 大写字母
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before, after)  # 创建映射表
    return s.translate(table)


s = input('请输入一个字符串：')
k = int(input('请输入一个整数密钥：'))
print(kaisa(s, k))
```

> 15 编写函数，接收任意多个实数，返回一个元组，其中最后一个元素为所有
参数的平均值，其他元素为所有参数中大于平均值的实数。

```python
def get_num():
    x = float(input("请输入一个实数(输入99999终止)："))
    k = [x]
    while abs(x - 99999) > 1e-3:
        x = float(input("请输入一个实数(输入99999终止)："))
        k.append(x)
    k.pop(len(k)-1)
    m = sum(k)/len(k)
    n = []
    for i in range(0, len(k)):
        if k[i] > m:
            n.append(k[i])
    n.append(m)
    n = tuple(n)
    return n


print(get_num())
```

> 16 编写函数，接收一个整数t为参数，打印杨辉三角前t行。要求居中。并
给出t为10的结果。

```python

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
```

# 五．（每小题4分，共20分）
           
> 17 编写函数，接收一个正偶数为参数，输出两个素数，并且这两个素数之和
等于原来的正偶数。如果存在多组符合条件的素数，则全部输出。

```python
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
```

> 18 向文本文件中写入内容，然后再读出。

```python
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
```

> 19 编写程序，保存为demo6.py，运行后生成文件demo6_new.py，其中的内
容与demo6.py一致，但是在每行的行尾加上了行号。

```python
filename = 'demo6.py'
with open(filename, 'r', encoding="utf-8") as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))

lines = [line.rstrip().ljust(maxLength) + '#' + str(index) + '\n'
         for index, line in enumerate(lines)]

with open(filename[:-3]+'_new.py', 'w', encoding="utf-8") as fp:
    fp.writelines(lines)
```

> 20 要求用户必须输入数字字符串。（要求利用异常处理结构）

```python
while True:
    x = input("请输入一个数字字符串：")
    try :
        x = int(x)
        print("你要输入的字符串是：%d" %x)
        break
    except Exception as e:
        print("产生异常！")
```