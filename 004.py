H, W = list(map(int, input().split()))
A = []
for i in range(H):
    row = list(map(int, input().split()))
    A.append(row)

row_sum = [0]*H
col_sum = [0]*W

# 行と列の和を計算
for i in range(H):
    row_sum[i] = sum(A[i])
    for j in range(W):
        col_sum[j] += A[i][j]

# 答えを出力
for i in range(H):
    ans = []
    for j in range(W):
        ans.append(row_sum[i]+col_sum[j]-A[i][j])
        if j == W-1:
            print(*ans)