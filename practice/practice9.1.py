class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is open now!')
    def desribe_restaurant(self):
        print(f"Hello! we are {self.restaurant_name} we have {self.cuisine_type}")
a=Restaurant("歪比巴卜","中国菜")
a.desribe_restaurant()
a.open_restaurant()
