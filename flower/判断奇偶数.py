import time as t
from time import sleep as s


def n(x):

    if x%2==0:
        
        print("偶数")
        return "偶数"
    if x%2==1:
        
        print("奇数")
        return "奇数"
if __name__=="__main__":    
    n(int(input()))
