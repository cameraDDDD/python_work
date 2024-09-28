class Bitch:
    def __init__(self,c,p):
        self.color=c
        self.cup=p
    def a1(self):
        print("I don't know what you say.")
class Big(Bitch):
    def __init__(self,c,p):
        super().__init__(c)
        self.p=p
        self.z=1
jb=Big(1,2)
print(jb.z)


