import random
# print(random.randint(1,100))
my_students=["nika","gabriel","dato","beka","elene"]
arr=["mercedes","toyota","bmw","audi","bugati"]
for i in range(len(my_students)):
    winner=random.choice(my_students)
    lucky_car=random.choice(arr)
    print(winner,"won the car",lucky_car)
    my_students.remove(winner)
    arr.remove(lucky_car)