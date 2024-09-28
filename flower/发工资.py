k,m=0,10000
for x in range(20):
    import random
    num=random.randint(1,10)
    k+=1#可以用x+1替换
    
    
    
    if num<5:
        print(f"员工{k},绩效分{num},低于5,不发工资,下一位.")
    else:
        m-=1000
        print(f"向员工{k}发放工资1000元,账户余额还剩{m}元.")
        if m<=0:
            
            print("工资发完了,下个月再领取吧.")
            break
            
        
        