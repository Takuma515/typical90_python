N, L = map(int, input().split())
steps = [0]*N
steps[0] = 1
mod = 10**9+7

for i in range(1,N):
    if i < L:
        steps[i] = steps[i-1] % mod
    else:
        steps[i] = (steps[i-1] + steps[i-L]) % mod

if N < L:
    print(steps[N-1])
else:
    print((steps[N-1]+steps[N-L]) % mod) 