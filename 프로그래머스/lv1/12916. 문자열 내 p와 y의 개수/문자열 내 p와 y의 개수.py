
def solution(s):
    countP = s.lower().count('p')
    countY = s.lower().count('y')
    if (countP == 0 and countY == 0): 
        return True
    elif (countP == countY):
        return True
    else:
        return False