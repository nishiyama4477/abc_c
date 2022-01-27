# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC161
# 仮説１：forループを回してmin_num 的なのを設定して更新していくプログラム
import math

n, k = map(int, input().split())

if n > k:
    when = math.ceil(n/k)
    # print(when, '回目で最小')
    min_n = abs(n - k*when)
    print(min_n)
else:
    zero = abs(n - k)
    one = abs(zero - k)
    print(min([zero, one]))







# if n >= k:
#     divided = n
#     divisor = k
# else:
#     divided = k
#     divisor = n
#
# left_or = divided % divisor
#
# print('あまりは', left_or)
#
# min_n = n
#
# for i in range(n):
#     a = abs(n-k)
#     # print('a is', a)
#     n = a
#     if min_n > a:
#         min_n = a
#
#
# print(min_n)
