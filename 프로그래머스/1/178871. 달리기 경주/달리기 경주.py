def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    for call in callings:
        i = result[call] 
        result[call] -= 1
        result[players[i-1]] +=1
        players[i-1], players[i] = players[i], players[i-1]
    return players