# 数据类型

## 1 数据类型转换

```python
a = int(input("请输入一个整数："))
```

强制类型转换为int

```python
int()
float()
str()
eval()
tuple()
list()
set()
dict()
```

## 2 Number

```text
int
float
bool
complex
+-*/ // % **  # 基本运算
```

## 3 String

1. 用单引号或双引号括起来。 
2. 索引从0开始； 
3. 字符串的切片：变量名[头下标:尾下标:步长] 左闭右开。

## 4 List

1. 用方括号[]括起来，元素之间用逗号,分隔。  
2. 切片索引同字符串，但是列表可以改变。
3. 常用方法：
   1. append(x)
   2. extend(L)
   3. insert(i, x)
   4. remove(x)
   5. pop(x)
   6. count(x)
   7. reverse()
   8. sort()  sort(reverse = True)
4. 常用函数：
   1. len()
   2. max()
   3. sum()
5. 成员资格判断in
6. 删除元素del
   1. 删除前三个元素 del L[:3]
   2. 删除偶数个元素 del L[::2]
7. 原地逆序 L.reverse()

## 5 Tuple

同数组，用小括号()分隔，不可变。

## 6 Dict

1. 大括号{}括起来，由键值对组成。
2. 读取：
   1. items()返回键值对
   2. keys()返回键
   3. values()返回值

## 7 Set

1. 大括号括起来。
2. 第13题，生成不重复随机整数，就可以通过检测列表长度是否等于集合长度，如果相等，则无重复元素。

## 8 推导式

### 8.1 列表推导式

```text
[表达式 for 变量 in 列表] 
[表达式 for 变量 in 列表 if 条件]
```

```python
import os # 列出所有py文件
x = [filename for filename in os.listdir('.') if filename.endswith('.py')]
print(x)
```

```python
# 实现矩阵转置
matrix = ...
matrix = [[row[i] for row in matrix] for i in range(4)]
```

### 8.2 字典推导式

```text
{ key_expr: value_expr for value in collection }
{ key_expr: value_expr for value in collection if condition }
```

### 8.3 集合推导式

列表推导式改成大括号。

### 8.4 元组推导式

列表推导式改成小括号。
