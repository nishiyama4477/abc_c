# ABC165

import sys
sys.setrecursionlimit(10 ** 5)
N, M, Q = map(int, input().split())
dat = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
print('dat is', dat)

def cal(p):
    num = 0
    for a, b, c, d in dat:
        if p[b - 1] - p[a - 1] == c:
            num += d
    return num




def dfs(num, p=[]):
    global ans
    if len(p) == N:
        ans = max(ans, cal(p))
        return
    for x in range(num, M + 1):
        dfs(x, p + [x])


for i in range(1, M + 1):
    print('started!')
    dfs(i)

print(ans)