# Removing Elements

#method 1
def remove_every_other(my_list):
    #return my_list[::2]

    arr1=[]
    i=0
    while i <len(my_list):
        arr1.append(my_list[i])
        i+=2
    return arr1

# method 2

def remove_every_other(my_list):
    arr = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            arr.append(my_list[i])
    return arr