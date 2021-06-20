N = int(input())
name_set = set()

for i in range(N):
    s = input()
    if s not in name_set:
        name_set.add(s)
        print(i+1)