def solution(friends, gifts):
    gift_jisoo = []
    givetake = []
    answer = []
    for _ in range(len(friends)):
        gift_jisoo.append([0,0,0])
        givetake.append([0]*len(friends))
        answer.append(0)
    
    for gift in gifts:
        a, b = gift.split(' ')
        a_index = friends.index(a)
        b_index = friends.index(b)
        
        # 선물 지수 구하기
        gift_jisoo[a_index][0]+=1
        gift_jisoo[b_index][1]+=1
        gift_jisoo[a_index][2] = gift_jisoo[a_index][0]-gift_jisoo[a_index][1]
        gift_jisoo[b_index][2] = gift_jisoo[b_index][0]-gift_jisoo[b_index][1]
        
        # 준사람 받은사람
        givetake[a_index][b_index]+=1
    
        
    for i in range(len(friends)-1):
         for j in range(i+1,len(friends)):
                if givetake[i][j] > givetake[j][i]:
                    answer[i] +=1
                elif givetake[i][j] < givetake[j][i]:
                    answer[j] +=1
                else: 
                    if (gift_jisoo[i][2] > gift_jisoo[j][2]):
                        answer[i] +=1
                    elif (gift_jisoo[i][2] < gift_jisoo[j][2]):
                        answer[j]+=1
                    else:
                        pass
                        
            
        
    return max(answer)