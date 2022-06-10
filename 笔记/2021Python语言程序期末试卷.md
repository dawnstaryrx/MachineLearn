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

> 3 编写函数，要求用户从键盘任意输入三个中文单词，按字典顺序输出。  

> 4 编写程序，把列表x = [a,b,a,b,a,b,a,b,a,b,a,b,a]中的所有a删掉。  


# 二．（每小题 5分，共20分）
　　　
> 5．使用列表推导式生成1000以内的最大的素数。  

```python
lis2 = [i for i in range(2, 1000)if 0 not in [i % j for j in range(2, int(i**0.5)+1)]]
print(lis2[-1])
```

> 6 编写函数，首先生成包含1000个随机字符的字符串，然后统计每个字符的出现次数。  


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

> 10 打印九九乘法表。要求：左对齐。

> 11 编写函数，要求输入一个数，判断一个这个数是否为素数。

> 12 编写程序，输出由1、2、3、4、5这五个数字组成的每位数都不相同的所有四位数。

# 四．（每小题4分，共20分）

> 13．编写程序，生成一个含有20个随机整数的列表，要求所有元素不相同，并且每个元素的值介于1到100之间。

> 14．凯撒加密，每个字母替换为后面第k个。（注意：小写字母循环小写字母，
大写字母循环大写字母）。

> 15 编写函数，接收任意多个实数，返回一个元组，其中最后一个元素为所有
参数的平均值，其他元素为所有参数中大于平均值的实数。


> 16 编写函数，接收一个整数t为参数，打印杨辉三角前t行。要求居中。并
给出t为10的结果。
         

# 五．（每小题4分，共20分）
           
> 17 编写函数，接收一个正偶数为参数，输出两个素数，并且这两个素数之和
等于原来的正偶数。如果存在多组符合条件的素数，则全部输出。

> 18 向文本文件中写入内容，然后再读出。

> 19 编写程序，保存为demo6.py，运行后生成文件demo6_new.py，其中的内
容与demo6.py一致，但是在每行的行尾加上了行号。

> 20 要求用户必须输入数字字符串。（要求利用异常处理结构）
