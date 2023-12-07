# How good are you really?

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return True if you're better, else False!

# method 1
def better_than_average(class_points, your_points):
    sum_class_points=0
    for i in class_points:
        sum_class_points+=i
    if sum_class_points/len(class_points)<your_points:
        return True
    return False

# method 2

def better_than_average(class_points, your_points):
    ave=sum(class_points)/len(class_points)
    if ave < your_points:
        return True
    else:
        return False
    
# method 3

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)