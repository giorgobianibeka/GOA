# Find the first non-consecutive number

# method 1
def first_non_consecutive(arr):
    my_arr=[]
    for i in range(0,len(arr)-1):
        if arr[i]== arr[i+1]-1:
            continue
        return arr[i+1]
    return None
#method 2

def first_non_consecutive(arr):
    i=0
    while i<len(arr)-1:
        if arr[i+1]-arr[i] !=1:
            return arr[i+1]
        i+=1