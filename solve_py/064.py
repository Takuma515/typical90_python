n, q = map(int, input().split())
A = list(map(int, input().split()))
B = [0]*n
ans = 0

for i in range(n-1):
    B[i] = A[i+1]-A[i]
    ans += abs(B[i])
B.append(0)

for i in range(q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    pre_diff = 0
    next_diff = 0
    if l != 0:
        pre_diff += abs(B[l-1])
        B[l-1] += v
        next_diff += abs(B[l-1])
    if r != n-1:
        pre_diff += abs(B[r])
        B[r] -= v
        next_diff += abs(B[r])
    
    ans += next_diff - pre_diff
    print(ans)
    