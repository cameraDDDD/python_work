clothes=['red pants','green pants','purple pants','orange pants','blue pants','write pants']
print(clothes)
input("Add yellow pants")
clothes.append('yellow pants')
print(clothes)
input("replace yellow pants with brown pants")
clothes[6]='brown pants'
print(clothes)
input("Appealing a pair of mysterious pants")
clothes.insert(-1,'GLOD PANTS')
print(clothes)
input("You dressed this gold pants")
del clothes[6]
print(clothes)
kevin=clothes.pop()
print(clothes)
print(f"The last pants is {kevin}")
a=input(6)
print(type(a))

