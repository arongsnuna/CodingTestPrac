def prime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for r in range(j+1, len(nums)):
                a=0
                a+=nums[i]+nums[j]+nums[r]
                if(prime(a)):
                    answer +=1  
    return answer