def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum=0
        for j in range(i,n+1):
            sum += j
            if (sum==n):
                answer +=1
                break
            elif (sum>n):
                break
            
    return answer
'''
def solution(n):
    answer = 0
    
    for i in range(n,0,-1):
        count = n
        for j in range(i,0,-1):
            count-=j
            if(count == 0): answer+=1
    return answer
'''