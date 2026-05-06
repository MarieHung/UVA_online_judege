T = int(input())
for i in range(T):
    ch = input()
    score = 0
    current = 0
    for c in ch:
        if c =="O":
            current +=1
            score += current
        else:
            current = 0
    print(score)

