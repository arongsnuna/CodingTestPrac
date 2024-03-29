numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
num =max(numbers)
print(num)
print(numbers.index(num)+1)