while True:
    try:
        a,b = map(int,input().split())
        ans = abs(a-b)
        print(ans)
    except EOFError:
        break
