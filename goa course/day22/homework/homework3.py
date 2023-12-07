# If you can't sleep, just count sheep!!

def count_sheep(n):
    sheep=""
    if n<1:
        return ""
    for i in range (1,n+1):
        sheep+=str(i)+" sheep..."
    return sheep