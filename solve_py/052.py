N = int(input())
mod = 10**9+7
ans = 1

for i in range(N):
    a_row = list(map(int, input().split()))
    a_sum = sum(a_row)
    ans = ans * a_sum % mod

print(ans)