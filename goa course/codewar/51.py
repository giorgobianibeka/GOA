#Total amount of points

def points(games):
    score=0
    for element in games:
        split_arr=element.split(":")
        if split_arr[0]>split_arr[1]:
            score+=3
        elif split_arr[0]==split_arr[1]:
            score+=1
    return score