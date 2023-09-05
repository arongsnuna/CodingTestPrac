def solution(food):
    answer = '0'
    for i in range(len(food)-1,0,-1):
        num = food[i]//2
        answer = str(i)*num + answer + str(i)*num
    return answer