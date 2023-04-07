def solution(n):
    n_list = list(map(str, str(n)))
    n_list.sort(reverse = True)
    return int(''.join(n_list))
