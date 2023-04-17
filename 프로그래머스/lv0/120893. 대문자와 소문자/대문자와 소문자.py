def solution(my_string):
    return my_string.swapcase()
    '''
    answer = ''
    for i in my_string:
        if(i.islower()):
            answer += i.upper()
        else:
            answer += i.lower()
    return answer
    '''