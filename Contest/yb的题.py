
def gcdx(x,y):#辗转相除判断x,y是否有大于1的公约数
    while True:
        r=y%x
        if r==0:
            if x==1:
                return False
            return True
        
        else:
            y=x
            x=r
def find(sum):#判断是否存在a,b有a+b=sum,gcdx(a,b)==True
    if sum<4:
        return False
    a=2
    b=sum-2#初始化
    while gcdx(a,b)==False and a>1 and b>1:
        a+=1
        b-=1
    if gcdx(a,b)==False:
        return False
    if gcdx(a,b)==True:
        return a,b

n=int(input(""))
for i in range(0,n):
    str_num=input("")
    l,r=str_num.split()
    l=int(l)
    r=int(r)
    while l<=r:
        if find(l):
            a,b=find(l)
            print(f"{a} {b}")
            break
        l+=1
    if l==r+1:
        print(-1)    




        







    
    
    
