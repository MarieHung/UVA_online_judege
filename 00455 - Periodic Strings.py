T = int(input())
for i in range(T):
    input()#用來吃掉空白行
    S = input()
    n = len(S)
    for k in range(1,n+1):
        #因為週期不可能是0，計算週期的時候要從0開始
        #而且因為最後判讀的時候要讀到第項，所以range要取到第n+1項
        if n%k == 0:
            pattern = S[:k]
            if pattern*(n//k) == S:#因為這個if 是在前一個條件成立之下寫的
                print(k)
                break
    if i != T-1:
        print()
        
