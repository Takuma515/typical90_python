H, W = map(int, input().split())
if H>1 and W>1:
    H = (H+1)//2
    W = (W+1)//2
print(H*W)