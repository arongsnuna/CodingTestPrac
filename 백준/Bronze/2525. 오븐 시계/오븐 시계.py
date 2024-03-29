hour, minute = map(int, input().split())
time = int(input())

minute += time
while minute >= 60:
    minute -= 60
    hour += 1
    while hour >= 24:
        hour -= 24
        
print(hour, minute)
