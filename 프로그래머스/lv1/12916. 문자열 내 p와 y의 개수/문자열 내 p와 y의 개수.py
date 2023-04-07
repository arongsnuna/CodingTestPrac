def solution(s):
    countP = 0
    countY = 0
    for i in range(0, len(s)):
        if (s[i]=='p' or s[i]=='P'):
            countP += 1
        if (s[i]=='y' or s[i]=='Y'):
            countY += 1
    if (countP == 0 and countY == 0): 
        return True
    elif (countP == countY):
        return True
    else:
        return False