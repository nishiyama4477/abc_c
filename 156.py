# 仮説　
#① X-Pの差を最小にしたい→Xの平均値を取ってそれをPとする
#②ここでPが小数点になったとき、例えば19.5を19とするか20とするか
# ↑成功した！ポイントはPをroundすること

N = int(input())
X = list(map(int, input().split()))

p = round(sum(X) / len(X))

total = 0

for i in X:
    ans = (i - p)**2
    total += ans

print(total)
