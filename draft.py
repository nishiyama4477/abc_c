# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC161
# 仮説１：forループを回してmin_num 的なのを設定して更新していくプログラム

n, k = map(int, input().split())

sample = n / k
# print(sample)

min_n = n

for i in range(n):
    a = abs(n-k)
    # print('a is', a)
    if min_n > a:
        min_n = a
        n = a

print(min_n)
