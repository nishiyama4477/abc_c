
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
        x_y.append(x)
        x_y.append(y)
        print('証言', j+1,  'は', x, y)
    testimonies.append(x_y)

print('testimonies is', testimonies)

for i in range(1, n+1):
    li = itertools.combinations(testimonies, i)

    comb = list(li)
    print(comb)
    print('取り出し方の種類は', len(comb))
    print(comb[0])
    for j in comb:
        count = [0] * n
        count[]

