def solution(s):
    answer = []
    newS = {}
    for i in range(len(s)):
        if(s[i] not in newS.keys()):
            answer.append(-1)
        else:
            answer.append(i-newS[s[i]])
        newS[s[i]] = i
    return answer