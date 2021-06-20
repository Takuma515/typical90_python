from collections import deque
Q = int(input())
deck = deque()
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
         # 山札の一番上(前)に入れる
         deck.appendleft(x)
    elif t == 2:
        # 山札の一番下(後ろ)に入れる
        deck.append(x)
    else:
        print(deck[x-1])