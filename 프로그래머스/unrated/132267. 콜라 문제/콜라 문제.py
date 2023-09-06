def solution(a, b, n):
    answer = 0
    # 빈병 a가 가져다주면 b개를 줌
    # n이 보유 병수
    # 보유 병수가 a개 미만이면 추가로 더 받을 수 없음
    while (n>=a):
        num = n//a
        answer += num*b
        n = n-num*a+num*b
    return answer