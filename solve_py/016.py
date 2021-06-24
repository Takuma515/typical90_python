N = int(input())
Coins = list(map(int, input().split()))
Coins.sort(reverse=True)

lim = min(9999, N // Coins[0])+1

ans = 10000
for i in range(lim):
    for j in range(10000):
        if N < Coins[0]*i+Coins[1]*j:
            break
        else:
            diff = N - (Coins[0]*i+Coins[1]*j)
            if diff % Coins[2] == 0:
                k = diff // Coins[2]
                ans = min(ans, i+j+k)

print(ans)