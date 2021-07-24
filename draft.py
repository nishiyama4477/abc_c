import math

# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')
#
# print(json.dumps(data))
import itertools
n, m, q = map(int, input().split())

Qs = [list(map(int, input().split())) for i in range(q)]

ran = [i for i in range(1, m+1)]

As = list(itertools.combinations_with_replacement(ran, n))

points = []

for j in range(len(As)):
    c = 0
    for k in range(q):
        if As[j][Qs[k][1] - 1] - As[j][Qs[k][0] - 1] == Qs[k][2]:
            c += Qs[k][-1]
    points.append(c)

print(points)

print(max(points))

