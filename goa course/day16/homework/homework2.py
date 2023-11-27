# Square(n) Sum

# Complete the square sum function so that it squares each
# number passed into it and then sums the results together.


def square_sum(numbers):
    my_sum=0
    for num in numbers:
        my_sum+=num**2
    return my_sum