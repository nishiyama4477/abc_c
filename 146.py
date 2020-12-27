a,b,x = map(int, input().split())

cri = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

for i in range(0, 9):
    if a * cri[i] + b * len(str(cri[i])) <= x and a * cri[i] - 1 + b * len(str(cri[i] -1)) <= x:
        continue
    else:
        r = len(str(cri[i])) -1
        print(r)
        break