N = int(input())

A_list = []
# 証言者ごとに集めた証言のリスト
xy_list = []
# 矛盾がなかった回答のカウンター
ans = 0
#
for i in range(N):
    A = int(input())
    xy = [list(map(int, input().split())) for _ in range(A)]
    xy_list.append(xy)

# 1<<Nと2**Nは一緒。
for st in range(1 << N):
    for witness, test in enumerate(xy_list):
        if not st >> witness & 1:
            continue

        for person, testimony in test:
            # 0-index
            person -= 1
            if st >> person & 1 != testimony:
                break

        else:
            continue

        break

    else:
        temp_r = bin(st).count('1')
        if temp_r > ans:
            ans = temp_r

print(ans)
