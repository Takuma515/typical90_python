import math

A, B = map(int, input().split())

LCM = A*B // math.gcd(A, B)
if  LCM > 10**18:
    print("Large")
else:
    print(LCM)