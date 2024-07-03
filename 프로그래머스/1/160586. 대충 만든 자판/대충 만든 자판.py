def solution(keymap, targets):
    answer = []
    keys = {}
    for k in keymap:
        for i, ch in enumerate(k):
            keys[ch] = min(i + 1, keys[ch]) if ch in keys else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in keys:
                ret = - 1
                break
            ret += keys[ch]
        answer.append(ret)

    return answer