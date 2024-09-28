#有问题
k=0

x=input('猜猜我的QQ账号是多少')

a=['1','5','1','1','2','4','9','8','5','9']
for b in a:
    for c in x:
        if b==c :
            k+=1

            print(k)