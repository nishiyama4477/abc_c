
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')

# 方針１
# まず人数から正直者である人の取り出し方を列挙。それに応じて数が多い順に、本当に正直者かを判定し、全て通ればそれが最大値。最後まで通らなければ0を出力。
import itertools

n = int(input())

h_or_un = []
for i in range(n):
    a = int(input())
    print('A is', a)
    x_y = []
    for j in range(a):
        x, y = map(int, input().split())
        x_y.append([x,y])
        print('x and y are', x, y)
    h_or_un.append(x_y)

print(h_or_un)

for i in range(1, n+1):
    li = itertools.combinations(h_or_un, i)
    print('list is', list(li))
