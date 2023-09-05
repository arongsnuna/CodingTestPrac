def solution(cards1, cards2, goal):
    a=0
    b=0
    leng = len(goal)
    for i in range(leng):
        if cards1[a]==goal[i]:
            if not(a==len(cards1)-1):
                a+=1
        elif cards2[b]==goal[i]:
            if not(b==len(cards2)-1):
                b+=1
        else:
            return "No"
    return "Yes"