def solution(n):
    answer = 1
    count = 0
    while(answer<=n):
        count += 1
        answer  *= count
        print(count, answer)
    return count-1