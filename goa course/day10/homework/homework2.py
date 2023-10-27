import random
list1=["!","@","#","$","%","^","&","*","(",")"]
list2=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
list3=["1","2","3","4","5","6","7","8","9","0"]
random_password=""
random_password2=""
for i in range(2):
    password=random.choice(list1)
    random_password+=password
for j in range(4):
    password2=random.choice(list2)
    random_password+=password2
for k in range(2):
    password3=random.choice(list3)
    random_password+=password3
print(random_password)
