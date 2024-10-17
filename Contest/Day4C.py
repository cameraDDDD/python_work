a=input()
line1=a.split()
length=int(line1[0])
zhushu=int(line1[1])
list_BIG=[]
for i in range(0,zhushu):
    i=input()
    linen=i.split()
    list_BIG.extend(linen)
list_num=[int(s) for s in list_BIG]
print(list_num)
x=min(list_num)
y=max(list_num)
print(x+length-y-1)

# 500 3
# 150 300
# 100 200
# 470 471

    



