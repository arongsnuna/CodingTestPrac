
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col
'''
def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if(sizes[i][0]<sizes[i][1]):
            sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
    w=sizes[0][0]
    h=sizes[0][1]
    for i in range(1,len(sizes)):
        if(w<sizes[i][0]):
            w=sizes[i][0]
        if(h<sizes[i][1]):
            h = sizes[i][1]   
    return w*h
'''