a=input()+" "

b=[]
d=[]
c=0
"""for i in a:
    b.append(i)
    print(b)"""

for x in a:
    
    if x==" ":
        
        e=len(d)
        while e>0:
            num=0
            for n in d:
                n=int(n)
                num+=n*10**(e-1)
                e-=1
            b.insert(0,num)
            #print(num)
            
        d.clear()
        continue
    
    d.append(x)
str_output=""
for dvd in b:
    if dvd != 0:    
        str_=str(dvd)
        str_output+=str_+" "
print(str_output)
    




        

        

