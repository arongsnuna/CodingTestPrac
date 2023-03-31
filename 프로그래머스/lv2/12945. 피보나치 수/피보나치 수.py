def solution(n):
    fibo = [0,1]
    if (n==0):
        answer=0
    elif (n==1):
        answer = 1
    else:
        for i in range(2,n+1):
            fibo.append(fibo[i-2]+fibo[i-1])
        answer = fibo[n]
    return answer %1234567