a=float(input('输入三角形的一边并回车'))
b=float(input('同上'))
c=float(input('同上'))
m=0.00000001

if a**2+b**2==c*c or b**2+c**2==a*a or c**2+a**2==c*c:
    print("这个三角形是直角三角形")
else:
    print("这个三角形不是直角三角形")