a=[1]
b=a
a=[2]#重新关联一个列表       #a.append(2)不行,因为a,b指向同一个列表
print(b)