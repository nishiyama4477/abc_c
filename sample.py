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

print(xy_list)
print(xy_list[0])
# 1<<Nと2**Nは一緒。つまりstはパターンを表す。
for st in range(1 << N):
    # witness は 人を表す。test は 証言。
    for witness, test in enumerate(xy_list):
        # ここはただのパターンの抽出。←違う説。
        if not st >> witness & 1:
            continue
        # それぞれのパターンに対してその証言が正しいか調べる
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
