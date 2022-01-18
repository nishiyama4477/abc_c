# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC160
# 仮説1：①隣り合う数の差をforで出し、それをlistにappendする。②listからlen(As)-1個取り出す組み合わせの中で最小のモノが答え。

from itertools import combinations

k, n = map(int, input().split())
As = list(int(i) for i in input().split())

distances = []

for i in range(len(As)):
    if i == len(As) - 1:
        v = As[i]
        # print('v is', v)
        dif = abs(k - v)
        # print('dif is', dif)
        distances.append(dif)
    else:
        v = As[i]
        v2 = As[i+1]
        dif = abs(v - v2)
        distances.append(dif)

# print('distances is', distances)

a = list(combinations(distances, 2))

# print('組み合わせは', a)

a_sum = list(sum(i) for i in a)

# print('それぞれ距離は', a_sum)

# print(a_sum)

print(min(a_sum))




