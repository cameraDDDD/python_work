my_food=["pizza","falafel","caarot cake","dick"]
friend_food=my_food[:3]
#不能用friend_food=my_food
for food in friend_food:
    print(food)
for food in my_food[3:]:
    print(food.upper())
print(my_food[0])