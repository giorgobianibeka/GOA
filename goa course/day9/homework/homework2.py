# Guri Jishkariani

# შევქმნათ ორი List-ი. ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების. 
# დავპრინტოთ დაწყვილებულად   😄 აი დააკომენტარეთ და დაგაწყვილებთო 
# რო იცოდნენ ფბზე ეგრე დაახლოებით  :დდდ

list=["beka","nika","giorgi","luka","guri"]
list2=["elene","nino","salone","mari","sofo"]
i=0
for name in list:
    print(str(list)+ " " + str(list2[i]))
    i+=1

girl_list=[]
boy_list=[]

for i in range(4):
    girl_name=input("enter girsl name: ")
    boy_name=input("enter boy name: ")

    girl_list.append(girl_name)
    boy_list.append(boy_name)