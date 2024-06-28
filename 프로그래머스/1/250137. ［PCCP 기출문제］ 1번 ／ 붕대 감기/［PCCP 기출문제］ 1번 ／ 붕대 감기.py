def solution(bandage, health, attacks):
    max_time = attacks[-1][0]
    blood = health
    band = 0
    attack_num=0
    for i in range(max_time+1):
        if(attacks[attack_num][0]==i):
            blood -= attacks[attack_num][1]
            band = 0
            attack_num+=1
            if(blood<=0):
                return -1
        else:
            band +=1
            blood += bandage[1]
            if(band == bandage[0]):
                blood+=bandage[2]
                band = 0
            if(blood>health):
                blood = health
            
    return blood
    