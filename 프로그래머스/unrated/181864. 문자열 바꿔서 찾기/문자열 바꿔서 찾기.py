def solution(myString, pat):
    return int(pat in myString.replace('A','C').replace('B','A').replace('C','B'))
    '''
    answer = ''
    for i in myString:
        if(i=='A'):
            answer += 'B'
        else:
            answer += 'A'
    return int(pat in answer)
    '''