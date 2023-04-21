def solution(myString):
    answer = ''
    for i in myString:
        if(i.isupper()):
            answer += i
        else:
            answer += i.upper()
    return answer