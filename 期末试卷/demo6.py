while True:
    x = input("请输入一个数字字符串：")
    try :
        x = int(x)
        print("你要输入的字符串是：%d" %x)
        break
    except Exception as e:
        print("产生异常！")