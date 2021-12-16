N, M = map(int, input().split())

# ここのflagはACが入ってきた時にTrueになる。　
flag = [False] * N
cnt = [0] * N
ans1, ans2 = 0, 0


for _ in range(M):
    p, S = map(str, input().split())
    p = int(p)

    if not flag[p - 1]:
        # これは初のACが入ってきたときの処理。
        if S == "AC":
            flag[p - 1] = True
            ans1 += 1
        # ACがなくWAのときは該当の問題のcntを1up
        else:
            cnt[p - 1] += 1

# ここでWAを決算してあげる。
for i in range(N):
    if flag[i]:
        ans2 += cnt[i]

print(ans1, ans2)
