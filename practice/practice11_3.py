class Employor:
    def __init__(self,first_name,last_name,salary):
        self.f_name=first_name
        self.l_name=last_name
        self.salary=salary
    def give_raise(self,add=5000):
        self.salary+=add
        

