def solution(park, routes):
    h, w = len(park), len(park[0])
    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if(park[i][j]=="S"):
                x,y = i,j
                break

    # 이동방향
    di = {'E':(0,1), 'W':(0,-1),'N':(-1,0), 'S':(1,0)}

    # 루트들
    for r in routes:
        direction, count = r.split(' ')
        dx, dy = x, y # 현재 위치

        for i in range(int(count)):
            nx = x + di[direction][0]
            ny = y + di[direction][1]

            if(0<=nx<=h-1 and 0<=ny<=w-1 and (park[nx][ny]!="X")):
                x, y = nx, ny

            else:
                x, y = dx, dy
                break

    return (x, y)