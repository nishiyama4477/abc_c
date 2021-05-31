# 仮説
# ①成立しない条件は大きく二つ（現段階では）
#   1：1桁目が0
#   2: 定義が二つある（s=1 c=3, s=1 c=2など）

n, m = map(int, input().split())
N = []
for i in range(n):
    N.append(0)
# print(N)

for i in range(m):
    s, c = map(int, input().split())
    # print('sは', s)
    # print('cは', c)
    if s == 1 and c == 0:
        print(-1)
        break
    elif N[s - 1] != 0:
        print(-1)
        break
    else:
        N[s - 1] = c

if N[0] != 0:
    print(N)