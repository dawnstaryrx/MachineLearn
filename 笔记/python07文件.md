# 文件

## 1 基本操作

* 文件按照数据的组织形式分为：文本文件和二进制文件。
* 文件内容操作三部曲：打开、读写、关闭。
* 基本操作：
  * 如果执行正常，open()函数返回一个可迭代的文件对象，通过该文件对象可以进行读写操作；否则抛出异常。 
  * `f1 = open("file1.txt", 'r', encoding = "UTF-8")`
  * 文件操作完成后，一定要关闭文件对象。这样才能保证所有修改被保存。
  * `f1.close()`
  * 即使写了关闭文件的代码，也无法保证文件一定能够正常关闭，推荐使用with关键字。
  * `with open("file.txt", 'r', encoding = "UTTF-8") as f:`

## 2 文件打开方式

* r  **默认**，**只读**，文件不存在抛出异常
* w  **只写**，若文件存在，则先清空原有内容
* x  写模式，创建新文件，如果文件已存在抛出异常
* a  **追加**
* b  **二进制**模式，可以与其他方式**组合**
* t  **默认**， 文本模式
* \+ 读写模式，可组合

## 例题

### 1 向文本文件写入内容，再读出

```python
s = "Hello world!"

with open("test.txt", 'w') as f:
    f.write(s)
with open("test.txt", 'r') as f:
    print(f.read())
```

### 2 读取并显示文本文件的前5个字符

```python
with open("test.txt", 'r') as f:
    s = f.read(5)
print("s = ", s)
print("字符串s的长度是 ", len(s))
```

### 3 读取并显示文本文件所有行

```python
with open("test.txt", 'r', encoding="UTF-8") as f:
    for line in f:
        print(line)
```

### 4 读取data.txt中的所有整数，升序排序后再写入data_asc.txt

```python
with open("data.txt", 'r') as fp:
    data = fp.readlines()
data = [int(line.strip()) for line in data]
data.sort()
data = [str(i) + "\n" for i in data]
with open("data_asc.txt", 'w') as fp:
    fp.writelines(data)
```