import random
# list=["todria","berashvili","giorgobiani","janashia",
# "kharatishvili","abuladze","kacitadze","lobjanidze",
# "goglichadze","guriko","hidd en","vishtekaliuki","gelashvili","neparidze",
# "miladze","papava","solomnishvili","zuzadze","sartania","motiashvili",
# "chxetiani","Wilashvili","labadze","solomonia","XXXX"]
score=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0]
for i in range(len(list)):
    students=random.choice(list)
print(students)
list.remove(students)
for student in students:
        answer=input("did the student answer correctly: ")
if answer=="yes":
        score[list.index(students)]+=10
else:
        score[list.index(students)]-=5
        print(score)
