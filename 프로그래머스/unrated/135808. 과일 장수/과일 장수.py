def solution(k, m, score):
    answer = 0
    #count = len(score)//m
    # for n in range(len(score)-1):
    #     for j in range(n+1,len(score)):
    #         if score[n]<score[j]:
    #             score[n], score[j]=score[j], score[n]
    score=sorted(score,reverse=True)
    for j in range(0,len(score),m):
        a=score[j:j+m]
        if(len(a)==m):
            answer += a[-1]*m
    return answer