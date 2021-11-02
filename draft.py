
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')

# 方針１
# N人の取り出し方それぞれに対して検証する。大きい数からやっていけば検証が通った途端にそれが答えとなる。
import itertools

n = int(input())

testimonies = []

for i in range(n):
    a = int(input())
    print('A is', a)
    x_y = []
    for j in range(a):
        x, y = map(int, input().split())
        pare = [x, y]
        x_y.append(pare)
        print('証言', j+1,  'は', x, y)
    testimonies.append(x_y)

print('testimonies is', testimonies)




# 一旦保留↓ とりまbit全探索でやってみる
#
#
# for i in range(1, n+1):
#     li = itertools.combinations(testimonies, i)
#
#     comb = list(li)
#     print(comb)
#     print('取り出し方の種類は', len(comb))
#     print(comb[0])
#     for j in comb:
#         count = [0] * n
#         count[]

#bit全探索でやってみる
# money = 300
# item = [('みかん', 100), ('りんご', 200), ('ぶどう', 300)]
#
# num = len(item)
#
# print(num)
#
#
# for i in range(2**num):
#     bag = []
#     for j in range(num):
#         if(i >> j) & 1:
#             bag.append(item[j][0])
#     print(bag)


for i in range(2**n):
    peo = []
    for j in range(n):
        if (i >> j) & 1:
            peo.append(testimonies[j])
    print('パターン', i, 'は', peo)
















