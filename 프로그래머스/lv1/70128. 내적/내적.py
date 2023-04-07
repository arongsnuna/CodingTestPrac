def solution(a, b):
    ss=0
    for i in range(len(a)):
        ss += a[i]*b[i]
    return ss