import pathlib
a=input("请输入你的名字")
p=pathlib.Path('guest.txt')
read=p.write_text(a)#会覆盖
