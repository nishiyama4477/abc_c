# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC162
# 仮説１：取り出すlistを作ってあげて、そこからitertoolsで取り出す。
import itertools
import random

k = int(input())

base = []

for i in range(3):
    num = []
    for j in range(1, k+1):
        num.append(j)
    base.append(num)

print(base[0])

ans = 0

for i in range(1, k+1):
    a = random.choice(base[0])
    b = random.choice(base[1])
    c = random.choice(base[2])
    added = sum([a, b, c])
    ans += added
    base[0].remove(a)
    base[1].remove(b)
    base[2].remove(c)

print(ans)



