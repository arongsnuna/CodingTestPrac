def solution(d, budget):
    d = sorted(d)
    answer = 0
    for i in range(len(d)):
        if(budget<d[i]):
            break
        else:
            budget -= d[i]
            answer +=1
    
    return answer