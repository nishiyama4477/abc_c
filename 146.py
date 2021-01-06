A, B, X = map(int, input().split())

# 買える判定↓
def is_ok(N):
    return A * N + B * len(str(N)) <= X


ok = 0
ng = 10 ** 9 + 1
# 隣合うまで
while ng - ok > 1:
    m = (ok + ng) // 2
    # 買えるなら左を動かす
    if is_ok(m):
        ok = m
    # 買えないなら右を動かす
    else:
        ng = m
# 小さい方を出力。←なぜかは分からない。。。
print(ok)
