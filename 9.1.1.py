class Friend:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def bark(self):
        print(f"{self.name} say 'woof'")
a=Friend("tzy","man")#self指a
a.lover="mee"
a.bark()
a.name
        