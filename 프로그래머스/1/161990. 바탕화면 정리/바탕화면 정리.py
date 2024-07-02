def solution(wallpaper):
    answer = [0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if (wallpaper[i][j]=='#'):
                if(len(answer)==1):
                    answer.extend([i,j,i+1,j+1])
                    answer.pop(0)
                else:
                    if(answer[0]>i):
                        answer[0]=i
                    if(answer[1]>j):
                        answer[1]=j
                    if(answer[2]<i+1):
                        answer[2]=i+1
                    if(answer[3]<j+1):
                        answer[3]=j+1
    return answer