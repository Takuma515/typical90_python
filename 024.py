N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

abs_sum = 0
for i in range(N):
    abs_sum += abs(A[i]-B[i])

if K >= abs_sum and (K-abs_sum)%2==0:
    print("Yes")
else:
    print("No")