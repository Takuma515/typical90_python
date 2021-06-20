N = int(input())
C1 = [0]*(N+1)
C2 = [0]*(N+1)
c1_sum = 0
c2_sum = 0

for i in range(1,N+1):
    c, p = map(int, input().split())
    if c == 1:
        c1_sum += p
    else:
        c2_sum += p
    C1[i] = c1_sum
    C2[i] = c2_sum

Q = int(input())
# クエリの処理
for i in range(Q):
    l, r = map(int, input().split())
    s1 = C1[r]-C1[l-1]
    s2 = C2[r]-C2[l-1]
    print(s1, s2)
