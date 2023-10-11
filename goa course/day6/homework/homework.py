# #1
score1=int(input("enter your score: "))
score2=int(input("enter your score: "))
score3=int(input("enter your score: "))
score4=int(input("enter your score: "))
sum_score=(score1+score2+score3+score4)/4
if sum_score>9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif sum_score<5:
    print("გილოცავ გაექეცი მატრიცას")
elif sum_score>5 and sum_score<9:
    print("YOU ARE MID")
else:
    sum_score<0 or sum_score>10
    print("there is something wrong with you")

#2
salary=int(input("enter your salary: "))
if salary>10000:
    print("გოა-ში სწავლობდი?")
elif salary>1000 and salary<10000:
    print("you mid")
else:
    print("შემოსულიყავი გოაში, მატრიცელო")