N, K = map(int, input().split())
scores = []

for i in range(N):
    a, b = map(int, input().split())
    scores.append(b)
    scores.append(a-b) # 部分点Bと(A-B)に分けて考える

scores.sort(reverse=True)
ans = 0
for i in range(K):
    ans += scores[i]    # 部分点の大きいものから解く

print(ans)