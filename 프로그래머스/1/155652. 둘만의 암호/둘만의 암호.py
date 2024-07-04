def solution(s, skip, index):
    a = ord('a')
    z = ord('z')
    all=[]
    for i in range(a,z+1):
        n = chr(i)
        if(n not in skip):
            all.append(n)
            
    all_dict ={}
    for i,letter in enumerate(all):
        all_dict[letter]=i
    print(all)
    print(all_dict)
    result=''
    for ss in s:
        n = all_dict[ss]+index
        result += all[n%len(all)]
    return result
        
        
        
    return answer