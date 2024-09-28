import random
items = ['剪刀','石头','布']
random_chioce=random.choice(items)
while True:
    a,b,c=0,0,0
    print(f"wins:{a}  losses:{b}  ties:{c}")
    d = input("剪刀 石头 布!!")#算了用c写
    