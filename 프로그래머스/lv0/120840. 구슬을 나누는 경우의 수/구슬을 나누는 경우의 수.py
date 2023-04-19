def solution(balls, share):
    b = balls
    s = share
    for i in range(balls-1,balls-share,-1):
        b *= i
    for j in range(share-1,0,-1):
        s *= j
    return b//s