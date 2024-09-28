from pathlib import Path
import json
mp =Path("账户余额.json")#创建json文件存储数据
"""d=20000
a=json.dumps(d)
mp.write_text(a)"""
con=mp.read_text()#读取数据
money=json.loads(con)#改格式并给money赋值

name="胡凯闻"

def n1():
    print(f"您的余额为{money}元.")
    input()
def n2():
    x=int(input("请输入您的存款金额:"))
    """global money
    money+=x"""
    global money
    money+=x
    mp.write_text(json.dumps(money))
    input(f"当前余额:{money}")

def n3():
    
    x = int(input("请输入您的取款金额:"))


    
    global money
    money-=x
    mp.write_text(json.dumps(money))
    input(f"当前余额:{money}")

n=input("请输入您的姓名:")
while name==n:
    try:
        i=int(input(f"----------主菜单----------\n{name},您好,欢迎来到奥特曼ATM,请选择操作\n查询余额 输入[1]\n存款 输入[2]\n取款 输入[3]\n退出 输入[4]\n请输入您的选择:"))
        if i==1:
            n1()
        if i==2:
            n2()
        if i==3:
            n3()
        if i==4:
            break
    except ValueError:
        break
    




