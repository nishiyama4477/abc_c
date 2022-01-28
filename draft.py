# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC161
# 仮説１：forループを回してmin_num 的なのを設定して更新していくプログラム
# 肝はどうやって例３を解くか。
import math

n, k = map(int, input().split())


# 前回のコード。勝手に法則を見つけたやつ。→解説を見た結果、近かった。n / k はボーダーで、そこからは数は２パターンしか取らないことを読み取る。
divided = math.floor(n / k)

base = n - k*divided

print(min(abs(base), abs(base - k)))







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
