# Opposites Attract

def lovefunc( flower1, flower2 ):
    if (flower1 % 2==0 and flower2 % 2==1)or (flower1 % 2==1 and flower2 % 2==0):
        return True
    return False

# Century From Year

def century(year):
    if year % 100==0:
        return year/100
    return year//100+1

# A Needle in the Haystack

# method 1

def find_needle(haystack):
    i=0
    for char in haystack:
        if char=="needle":
            return("found the needle at position {}".format(i))
        i+=1

# method 2
def find_needle(haystack):
    my_arr = haystack.index("needle")
    return "found the needle at position " + str(my_arr)