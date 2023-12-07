# Sum of positive

# ou get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    my_arr=0
    for element in arr:
        if element>0:
            my_arr+=element
    return my_arr