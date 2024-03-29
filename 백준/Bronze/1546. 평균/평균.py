a=int(input()) 
inn=input()
nums =[]
summ = 0

for i in range(a):
    nums.append(int(inn.split()[i]))
max_num = max(nums)
for i in nums:
    summ += i/max_num*100
    
print(summ/a)
