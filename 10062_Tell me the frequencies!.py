from collections import Counter
first = True
while True:
    try:
        line = input()
        if not first:
            print()   # 印空行
        first = False
        count = Counter(line)
        x= list(count.items())
        x.sort(key= lambda x:(x[1],-ord(x[0])))
        for ASC, freq in x:
            print(ord(ASC),freq)
    except EOFError:
        break
        
