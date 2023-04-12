def solution(t, p):
    a = len(p)
    answer = 0
    for i in range(len(t)-a+1):
        b = t[i:i+a]
        if(int(b)<=int(p)):
            answer+=1
    return answer