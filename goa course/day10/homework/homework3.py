import random
name=["beka","nika","irakli","elene"]
score=[0,0,0,0]
answer=input("enter pasuxi:")
for i in range(len(name)):
    students=random.choice(name)
    print(students)
    name.remove(students)
# if answer=="yes":
#     score[name.index(students)]+=10
# else:
#     score[name.index(students)]-=5
# print(score)