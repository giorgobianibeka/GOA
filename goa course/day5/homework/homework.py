#1
age=int(input("enter your age: "))
dad_age=int(input("enter your dad age: "))
year=int(input("enter interesed year: "))
for i in range(year-2023):
    new_age=(dad_age+i)//(age+i)
    print(str(2023+i)+" wels iqneba "+str(new_age)+" jer didi ")

#2
i=0
while i<30:
    i+=1
    if i%2==0:
        print(str(i)+" luwi")
    else:
        print(str(i)+ " kenti")

#2 metod-2
for i in range(30):
    if i%2==0:
        print(str(i)+" luwi")
    else:
        print(str(i)+" kenti")
#metod-3
n=2
x=1
while n<=30:
    print("რიცხვი "+ str(x)+" არის კენტი")
    print("რიცხვი "+str(n)+" არის ლუწი")
    n+=2
    x+=2