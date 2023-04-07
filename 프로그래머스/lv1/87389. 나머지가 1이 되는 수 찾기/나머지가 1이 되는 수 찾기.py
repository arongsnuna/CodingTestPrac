def solution(n):
    # n%x = 1 중에서 가장 작은 x
    for i in range(2, n):
        if (n%i==1):
            return i