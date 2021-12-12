# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC150
import itertools

n = int(input())

lia = list(map(int, input().split()))

lib = list(map(int, input().split()))


li = [i for i in range(1, n+1)]

a = 0
b = 0

permutations = list(itertools.permutations(li, n))
# print('permutationsは', permutations)
for i, v in enumerate(permutations):
    if v == tuple(lia):
        # print('発見！')
        a = i+1
    if v == tuple(lib):
        # print('発見！')
        b = i+1

print(abs(a-b))