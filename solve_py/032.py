from itertools import permutations

N = int(input())
A = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

M = int(input())
isBad = []  # 隣接行列
for _ in range(N):
    isBad.append([0]*N)

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    isBad[x][y] = 1
    isBad[y][x] = 1

ls = list(permutations(range(0,N))) # 順列生成
ans = 10**10

# 順列全探索
for per in ls:
    sum = 0
    for i in range(N):
        if isBad[per[i-1]][per[i]] and i != 0:
            sum = 10**10
            break
        sum += A[per[i]][i] #選手per[i]がi区を走る
    ans = min(ans, sum)

if ans == 10**10:
    print(-1)
else:
    print(ans)

