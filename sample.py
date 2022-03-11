# ABC165

import sys
sys.setrecursionlimit(10 ** 5)
N, M, Q = map(int, input().split())
dat = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
print('dat is', dat)

# これはdfs時にifに引っかかった時だけに作用するfunc
# dfsで出てきたAをquadsで点数づけ
# ここでいうnumは点数


def cal(p):
    num = 0
    for a, b, c, d in dat:
        if p[b - 1] - p[a - 1] == c:
            num += d
    return num


# ここではp=Aとして値を取り出し、その都度点数を更新する

A_counter = 0


def dfs(num, p=[]):
    global ans
    global A_counter
    global counter
    if len(p) == N:
        print('ーーーーーーーーーーー')
        A_counter += 1
        ans = max(ans, cal(p))
        return
    # ここでAを作る。
    for x in range(num, M + 1):
        print('dfs_stareted!', 'x = ', x)
        counter += 1
        dfs(x, p + [x])


for i in range(1, M + 1):
    counter = 0
    print('started!', 'i = ', i)
    dfs(i)

print(A_counter)
print(ans)