def solution(phone_number):
    leng = len(phone_number)
    answer = '*'*(leng-4)+phone_number[-4:]
    return answer