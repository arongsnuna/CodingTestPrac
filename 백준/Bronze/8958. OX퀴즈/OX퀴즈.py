i = int(input())
answer = []
for _ in range(i):
    text = input()
    score = 0
    total = 0
    for t in text:
        if t == "O":
            score +=1
            total += score
        elif t=="X":
            score =0
    answer.append(total)
            
for n in range(i):
    print(answer[n])