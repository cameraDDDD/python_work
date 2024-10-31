# def dv(x):#普通递归
#     if x==1:
#         return 1
#     sum=dv(x-1)
#     return x**2+sum
# print(dv(10))
def dv(x,sum):
    if x==0:
        return sum
    return dv(x-1,sum+x**2)
print(dv(10,0))

