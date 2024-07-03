def solution(keymap, targets):
    answer = []
    keys ={}
    for key in keymap:
        for l in range(len(key)):
            if key[l] not in keys:
                keys[key[l]] = l+1
            else:
                if(keys[key[l]]>l+1):
                    keys[key[l]]=l+1
    for target in targets:
        a=0
        for t in target:
            if(t not in keys):
                a=-1
                break
            else:
                a+=keys[t]
        answer.append(a)
    return answer