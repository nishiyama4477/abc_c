# ABC157 解答

n, m = map(int, input().split())

t = [-1] * n

for i in range(m):
    s, c = map(int, input().split())
    # インデックスのために-1
    s -= 1

    # 予想が二つ出来たらprint(-1)。同じ予想だったらそのまま続行。
    # t[s] != -1というのは値が入っていないということ。
    if t[s] != -1 and t[s] != c:
        print(-1)
        exit()

    t[s] = c

print(t)

# ２桁いじょうの時
if n != 1:
    # ２桁以上の整数で最初の桁の予想が0の場合もある。なぜなら0<=c<=9だから。
    if t[0] == 0:
        print(-1)
        exit()
    if t[0] == -1:
        t[0] = 1

    for i in range(1, n):
        if t[i] == -1:
            t[i] = 0
else:
    if t[0] == -1:
        t[0] = 0

print(''.join(map(str, t)))

t = [-1] * n

for i in range(m):
    pre, val = map(int, input().split())
    pre -= 1
    if t[pre] != -1 and t[pre] != val:
        print(-1)
        exit()

    t[pre] = val

# print(t)

if n != 1:
    if t[0] == 0:
        print(-1)
        exit()
    if t[0] == -1:
        t[0] = 1

    for i in range(1, n):
        if t[i] == -1:
            t[i] = 0
else:
    if t[0] == -1:
        t[0] = 0
# print(t)

print(''.join(map(str, t)))
