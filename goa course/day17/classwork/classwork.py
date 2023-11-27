# my_str="baskjdnqowdnajsndasbdklncalsbyqbed,ajsnkcmas"
def str_count(str,char): # we defined a function needed
                        #str_count and we created two parametres
    list=[]  # we created an empty list
    list.append(char) # we appended the value of variable "char" in our empty list
    for i in str:  # we did a for loop in our string
        if char==i:  # we check it our variable "char" equals to iteration variable i
            list.append(i) # if the statemant above is True we append our iteration variable in the list
    return len(list)-1 # this function returns an integer calculates the lenght of the list and
                        #subtrackts one
print(str_count('hellllo',"l")) # we call the function and pass two arguments

def str_count_chad(str,my_char):
    counter=0
    for char in str:
        if char==my_char:
            counter+=1
    return counter
print (str_count_chad("my_str","l"))



# Counting sheep...


# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    amount_of_sheep=0
    for element in sheep:
        if element==True:
            amount_of_sheep+=1
    return amount_of_sheep

# You Can't Code Under Pressure #1

#  Code as fast as you can! You need to double the integer and return it.


def double_integer(i):
    return i*2