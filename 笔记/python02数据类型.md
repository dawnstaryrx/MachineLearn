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

用单引号或双引号括起来。
索引从0开始；
字符串的切片：变量名[头下标:尾下标] 左闭右开。

## 4 List

用方括号括起来，元素之间用逗号分隔。
同字符串，但是可以改变。

## 5 Tuple

同数组，用小括号分隔，不可变。

## 6 Dict

大括号括起来，由键值对组成。

## 7 Set

大括号括起来。

## 8 推导式

### 8.1 列表推导式

```text
[表达式 for 变量 in 列表] 
[表达式 for 变量 in 列表 if 条件]
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
