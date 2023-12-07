# Counting sheep...


# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    amount_of_sheep=0
    for element in sheep:
        if element==True:
            amount_of_sheep+=1
    return amount_of_sheep