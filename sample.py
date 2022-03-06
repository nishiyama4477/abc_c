# ABC165

from itertools import combinations_with_replacement as comb_rplc
import numpy as np

n, m, q = map(int, input().split())

lines = [[]]
lines[0] = list(map(int, input().split()))

for i in range(q - 1):
    lines.append(list(map(int, input().split())))
# linesは条件のリスト
print('lines is', lines)

# Aの要素のとりうる値の範囲を出力
range_arry = np.arange(1, m + 1)
print('range_arry is', range_arry)
a = comb_rplc(range_arry, n)
print('全パターンは', a)

total = []
# ここでいうcombはパターン一つ一つのこと。
for i, comb in enumerate(a):
    total.append(0)
    for line in lines:
        # 以下は条件にあっているかどうかチェック。あっていればc（line[3])を得点として追加.
        if comb[line[1] - 1] - comb[line[0] - 1] == line[2]:
            total[i] += line[3]
print(max(total))