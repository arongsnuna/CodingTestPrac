def solution(name, yearning, photo):
    answer = []
    sumA = 0
    for ls in photo:
        for person in ls:
            if person in name:
                sumA+=yearning[name.index(person)]
        answer.append(sumA)
        sumA=0
    return answer