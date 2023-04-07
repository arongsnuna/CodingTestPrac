def solution(x):
    ss = list(map(int,str(x)))
    hap = 0
    for i in ss:
        hap += i
    if (x%hap==0):
        return True
    else:
        return False
