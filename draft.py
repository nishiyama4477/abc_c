# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC165
# 仮説１
# ステップを分けると、①Aのとりうる値を決める。②点数を判定し、より大きければ更新。←でも多分①の段階でおおよそのとりうる値的なのは見つけられそう。
# というより、Asからある程度数字を予測できそうな気もする。=cになるようにAを作れば良いだけ。
# 組み合わせの考え方を使えばいけそう。
# 2月13日の考え方。
# ①条件からそれぞれの値の候補を見つける。②条件から絞られた候補の中で組み合わせていく。
# 2月17日更新
# 多分これはbit全探索や。おそらく①まずbit全探索でパターンを網羅する。②それぞれのパターンについて条件を満たす数字が存在するか調べる。


# n, m, q = map(int, input().split())
# quads = []
#
# for i in range(q):
#     quad = list(int(i) for i in input().split())
#     quads.append(quad)
#
# print(quads)
#
# N = len(quads)
#
# most = 0
#
# for i in range(2**N):
#     pattern = []
#     print('pattern{}:'.format(i))
#     for j in range(N):
#         if (i >> j) & 1:
#             pattern.append(quads[j])
#             base = m - quads[j][2]
#             for s in range(0, base):
#                 b = m - s
#                 a = s+1
#
#
#
#     print(pattern)





    # if result >= most:
    #     most = result




#　↑このquadsに関してbit全探索でパターンを網羅する。


# 仮説２：まず確認したい条件が３つ。①b > aである（index高ーindex低である）②c < m(cは少なくともAのとりうる最大値から１は引かれている）
# ③条件が被ることはない。（a1, b1, c1)　!= (a2, b2, c2)
from itertools import combinations_with_replacement as comb_repl
import numpy as np
n, m, q = map(int, input().split())

quads = [[]]
quads[0] = list(map(int, input().split()))

for i in range(q-1):
    quads.append(list(map(int, input().split())))

# print(quads)

comb_range = np.arange(1, m+1)
# print(comb_range)

a = comb_repl(comb_range, n)

total = []

for i, comb in enumerate(a):
    total.append(0)
    for quad in quads:
        if comb[quad[1]-1] - comb[quad[0]-1] == quad[2]:
            total[i] += quad[3]

print(max(total))















