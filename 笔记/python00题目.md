# 2

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