def solution(today, terms, privacies):
    answer = []
    terms_dict={}
    for t in terms:
        a, b= t.split(" ")
        terms_dict[a]=int(b)*28-1 if(int(b)>0) else 0
    for i, p in enumerate(privacies):
        date, term = p.split(" ")
        y,m,d = date.split(".")
        y, m, d = int(y), int(m), int(d)
        d += terms_dict[term]
        while(d>28):
            m += 1
            d -= 28
            while(m>12):
                y += 1
                m -= 12
        ty, tm, td = today.split(".")
        ty,tm,td = int(ty), int(tm), int(td)
        if(ty>y):
            answer.append(i+1)
        elif(ty==y and tm>m):
            answer.append(i+1)
        elif(ty==y and tm==m and td>d):
            answer.append(i+1)
        
    return answer