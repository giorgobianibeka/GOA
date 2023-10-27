#Merab Tsitskhvaia

# User-ს შემოატანინეთ თავისი სიმაღლე. მიეცით საშუალება მომხმარებელს აირჩიოს ის, 
# თუ რომელ სიდიდეში სურს გაიგოს თავისი სიმაღლე, სანტიმეტრებში თუ ფუნტებში...
# (თუ შემოიტანს 180-ს და აირჩევს ფუტებში გადაყვანას თავისი წონის, დაუპრინტეთ რამდენი ფუტია ის. 

user=int(input("if you want cm answer 0 if you ft answer 1: "))
height=0
if user==0:
    height1=int(input("enter your height cm: "))
    print("you are "+ str(height1*0.032808399)+" ft")
else:
    user==1
    height2=int(input("enter your height ft: "))
    print("you are "+str(height2*30.48)+" cm")