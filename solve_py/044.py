N, Q = map(int, input().split())
A = list(map(int, input().split()))
shift = 0

for i in range(Q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:  
        # swap
        x = (x-shift) % N
        y = (y-shift) % N
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        # shift
        shift += 1
    else:
        x = (x-shift) % N
        print(A[x])
    