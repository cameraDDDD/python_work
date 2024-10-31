# 对函数嵌套以及闭包的探究
def fun1(a):
    print("fun1 is used ",a)
    def fun2(b):
        print("fun2 is used ",b)
        def fun3(c):
            print("fun3 is used ",c)
            return fun2
        return fun3
    return fun2

a = fun1(1)(2)(3)
a(2)