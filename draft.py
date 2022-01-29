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
divided = n % k
# print(divided)
more = abs(divided - k)

print(min(divided, more))

