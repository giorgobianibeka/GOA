# რატი მურღულია

# მომხმარებელს შემოატანინეთ ორი სახელი და გვარი,
# და შეადარეთ ერთი მეორეს,დაითვალეთ a-ს რაოდენობა 
# რომელ სახელში არის მეტი,და დაპრინტეთ მიღებული შედეგი/


name=input("enter your full name: ").lower()
name2=input("enter your full name: ").lower()
amount_a=0
amount_a2=0
for i in name:
    if i=="a":
        amount_a+=1
for i in name2:
    if i=="a":
        amount_a2+=1
if amount_a>amount_a2:
    print("პირველ სახელში არის მეტი ა ")
elif amount_a<amount_a2:
    print("მეორე სახელში არის მეტი ა")
else:
    print("თანაბარი რაოდენობის ა")
