#ninosolomonia

# შექმენით მეოთხე ჯგუფის წევრების სია .დაწერეთ კოდი ისე,
# რომ გაიგოთ ყველა სახელსა და გვარში ერთად რამდენი  ,,ი" და ,,ა"   იქნება.

list=["ალექსანდრე თოდრია","ბექა ბერაშვილი","ბექა გიორგობიანი","დავით ჯანაშია","დემეტე ხარატიშვილი","გაბრიელ მოლოდინი","გიო აბულაძე"]
counter_a=0
other_char=0
counter_i=0
for element in list:
    for char in element:
        if char == "ი":
            counter_i+=1
        elif char == "ა":
            counter_a+=1
        else:
            other_char+=1
print(counter_a,counter_i,other_char)