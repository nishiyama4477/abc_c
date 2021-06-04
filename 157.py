# 仮説
# ①成立しない条件は大きく二つ（現段階では）
#   1：1桁目が0
#   2: 定義が二つある（s=1 c=3, s=1 c=2など）

n, m = map(int, input().split())

t = [-1] * n

for i in range(m):
    s,c = map(int, input().split())
    # ここのsはindex値↓
    s -= 1

# このifは’定義が二つ以上あった場合'（上記の2）の処理。つまり①: なにか値が入っていて、②: かつさらに新しい値が入ってこようとしている時
    if t[s] != -1 and t[s] != c:
        print(-1)
        exit()

    t[s] = c

# nが2桁以上の時は
if n != 1:
    # 先頭が0であればダメ
    if t[0] == 0:
        print(-1)
        exit()
    # 先頭が何も入っていなかったら1
    if t[0] == -1:
        t[0] = 1

    # 先頭以外の値で何も入っていない時は0
    for i in range(1, n):
        if t[i] == -1:
            t[i] = 0
# 1桁の時何も入っていなかったら0、それ以外は0でも良いので放置
else:
    if t[0] == -1:
        t[0] = 0

print(''.join(map(str, t)))




