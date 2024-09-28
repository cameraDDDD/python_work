while True:
    try:
        a=int(input("请再输入一个数字:"))
        b=int(input("请再输入一个数字:"))
        c=a+b
        print(f"两个数字加起来等于:{c}")

    except (ValueError,NameError) :
        print("这他妈不是数字")


