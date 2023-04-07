def solution(absolutes, signs):
    ss=0
    for i in range(len(signs)):
        if(signs[i]==False):
            ss+=(-1)*absolutes[i]
        else:
            ss+=absolutes[i]
    return ss