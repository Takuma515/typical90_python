import math
A, B, C = map(int, input().split())
abc_gcd = math.gcd(A, B)
abc_gcd = math.gcd(abc_gcd, C)
A //= abc_gcd
B //= abc_gcd
C //= abc_gcd

print(A+B+C-3)
