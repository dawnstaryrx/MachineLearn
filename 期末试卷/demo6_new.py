while True:                      #0
    x = input("请输入一个数字字符串：")     #1
    try :                        #2
        x = int(x)               #3
        print("你要输入的字符串是：%d" %x) #4
        break                    #5
    except Exception as e:       #6
        print("产生异常！")           #7
