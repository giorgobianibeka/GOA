# A Needle in the Haystack

#Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# method 1
def find_needle(haystack):
    my_arr = haystack.index("needle")
    return "found the needle at position " + str(my_arr)

# method 2

def find_needle(haystack):
    i=0
    for char in haystack:
        if char=="needle":
            return("found the needle at position {}".format(i))
        i+=1