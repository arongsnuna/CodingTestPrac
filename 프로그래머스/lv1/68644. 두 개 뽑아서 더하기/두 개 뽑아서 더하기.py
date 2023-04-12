def solution(number):
    from itertools import combinations
    answer = []
    for i in combinations(number,2):
        if(sum(i) not in answer):
            answer.append(sum(i))
    return sorted(answer)
'''
def solution(number):
    answer = []
    for i in range(len(number)):
        for j in number[i+1:]:
            if(number[i]+j not in answer):
                answer.append(number[i]+j)
    return sorted(answer)
'''