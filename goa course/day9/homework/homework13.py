#nino goglichadze 


# შემოიტანეთ სამი რიცხვი და დაპრინტეთ გამოვა თუ არა ამ რიცხვების საშუალებით სამკუთხედი, 
# თუ გამოვა გამოთვალეთ პერიმეტრი და დაპრინტეთ "ამ სამკუტხედის პერიმეტრია: XX" 
# თუ არ გამოდის მაშინ დაპრინტეთ „მსგავსი სამკუთხედი არ არსებობს“
number1=int(input("enter side"))
number2=int(input("enter side"))
number3=int(input("enter side"))
if (number1+number2>number3 and number1+number3>number2 and number2+number3>number1):
    print("ამ სამკუთხედის პერიმეტრია: "+ str(number1+number2+number3))
else:
    print("მსგავსი სამკუთხედი არ არსებობს")