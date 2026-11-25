while True:
    try:
        a,b = map(int,input().split())
        if a <=2**63 and b<=2**63:
            #abs()絕對值
            x = abs(b-a)
            print(x)
    except EOFError:
        break
