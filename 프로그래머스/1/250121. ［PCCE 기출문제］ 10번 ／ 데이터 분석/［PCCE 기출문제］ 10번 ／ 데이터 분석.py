def solution(data, ext, val_ext, sort_by):
    fra = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    ki = fra[ext]
    so = fra[sort_by]
    dap = []
    for d in data:
        if (d[ki] < val_ext):
            dap.append(d)
    dap.sort(key = lambda x : x[so])  
        
    return dap