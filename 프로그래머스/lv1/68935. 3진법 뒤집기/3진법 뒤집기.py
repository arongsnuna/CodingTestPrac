def solution(n):
    answer = ''
    while n:
        answer += str(n%3)
        n//=3
    dap = 0
    for i in range(len(answer)):
        dap += 3**(len(answer)-i-1)*int(answer[i])
    return dap