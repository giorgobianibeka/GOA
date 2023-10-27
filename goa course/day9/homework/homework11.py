#Luka Siradze
# input ფუნქციით შემოატანინეთ წინადადება და შმოტანილ წინადედებაში პროგრამას დაათვლევინეთ თანხმოვნები
text=input("etner some word: ")
text=text.lower()
vowels=0
consonants=0
for i in text:
    if (i=="a" or i=="e" or i=="i" or i=="o"or i=="u"):
        vowels=vowels+1
    else:
        consonants=consonants+1
print("your text in "+str(consonants)+" consonants")
print("your text in "+str(vowels)+" vowel")