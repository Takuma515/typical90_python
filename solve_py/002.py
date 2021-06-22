N = int(input())

if N%2==1:
    exit(print())
ALL = 1 << N
def has_bit(n, i):
    return (n>>i) & 1

ans = []
for n in range(ALL):
    left_num = 0
    s = ''
    for i in range(N):
        if has_bit(n, i):
            left_num += 1
            s += '('
        else:
            left_num -= 1
            s += ')'
        if left_num < 0:
            break
    if left_num == 0:
        ans.append(s)

ans = sorted(ans)
for s in ans:
    print(s)