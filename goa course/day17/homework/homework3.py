# Returning Strings

#Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".


#   method 1
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

# method 2

def greet(name):
    return "Hello, " + name + " how are you doing today?" 