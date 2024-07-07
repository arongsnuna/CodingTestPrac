def solution(babbling):
    answer = 0
    alls = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for can in alls:
            if( can in b):
                if(can*2 not in b):
                    b=b.replace(can,' ')
        if(b.isspace()):
            answer+=1
    return answer