while True :
    try:
        T = int(input())
        for i in range(T):
            N = int(input())
            money = 0
            for j in range(N):
                #a農場面積
                #b農場裡動物數目，這個數字用不到
                #c環保等級
                a,b,c = map(int,input().split())
                money += a*c
            print(money)

    except EOFError:
        break
