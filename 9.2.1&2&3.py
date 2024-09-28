class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=149
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self,adding_mileage):
        if adding_mileage>=0:
            self.odometer_reading+=adding_mileage
        else:
            print("You wanna play a trick on me?Son of bitches?")
my_new_car=Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1)
my_new_car.update_odometer(100)

my_new_car.read_odometer()