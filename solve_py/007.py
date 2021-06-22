import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort() # 二分探索のためにソート

Q = int(input())
for i in range(Q):
    B = int(input())
    bi_left = bisect.bisect_left(A, B)
    ans = 0
    if bi_left == 0:
        ans = abs(A[0]-B)
    elif bi_left == N:
        ans = abs(A[N-1]-B)
    else:
        ans = min(abs(A[bi_left-1]-B), A[bi_left]-B)
    print(ans)


