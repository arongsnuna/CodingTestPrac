def solution(n, m):
    answer = []
    if (n<m):
        n,m = m,n
    for i in range(n,0,-1):
        if(n%i==0 and m%i==0):
            answer.append(i)
            break
    mm = (n//answer[0])*(m//answer[0])*answer[0]
    answer.append(mm)

    return answer