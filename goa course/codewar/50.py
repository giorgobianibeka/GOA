# Sum without highest and lowest number

# method 1
def sum_array(arr):
    if arr==None or len(arr)<3:
        return 0
    return sum(arr)-max(arr)-min(arr)

    # method 2
    def sum_array(arr):
        if not arr:
            return 0
        elif len(arr)<2:
            return 0
    print(arr)
    arr.sort()
    arr.pop(0)
    arr.pop(-1)
    
    return sum(arr)