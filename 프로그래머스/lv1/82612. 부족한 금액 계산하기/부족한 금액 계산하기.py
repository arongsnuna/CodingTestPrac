def solution(price, money, count):
    return max(0, price*(count+1)*(count)//2-money)
    '''
    hap = 0
    for i in range(1,count+1):
        hap += price*i
    answer = 0 if(money >hap) else hap-money

    return answer'''