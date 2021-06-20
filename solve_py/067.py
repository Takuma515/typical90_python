import numpy as np
N, K = map(int, input().split())

for _ in range(K):
    N = int(str(N), 8) # 10進数
    N = np.base_repr(N, base=9) # 9進数(str)
    N = N.replace('8', '5') # 8進数

print(N)