def solution(k, score):
    answer = []
    sorting = []
    # 상위 k번째 이내 -> 명예의 전당
    for s in score:
        sorting.append(s)
        sorting.sort(reverse=True)
        if(len(sorting)<k):
            answer.append(sorting[-1])
        else:
            answer.append(sorting[k-1])
    return answer