#ანრი ზუბაშვილი

# [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
# იპოვეთ ყველაზე პატარა რიცხვი აქ
# min() ფუნქციის გამოყენების გარეშე

list=[ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
list.sort()
print(list[0])

# method 2
list=[ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
list_min=list[0]
for num in list:
    if num<list_min:
        list_min=num
print(list_min)