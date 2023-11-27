def summation(num):
    my_sum=0
    for i in range(1,num+1):
        my_sum+=i
    
#Beginner Series #2 Clock

def past(h, m, s):
    return (h*3600+m*60+s)*1000


# Beginner Series #1 School Paperwork

def paperwork(n, m):
    if n<0 or m<0:
        return 0
    return n*m

# Abbreviate a Two Word Name
def abbrev_name(name):
    my_list=name.split()
    return my_list[0][0].capitalize() + "." + my_list[1][0].capitalize()

my_str="hello world"
my_arr=my_str.split()
str1=my_arr[0]
str2=my_arr[1]

print(str1)
print(str2)