
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')
#
# print(json.dumps(data))
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
PS = [input().strip().split() for i in range(M)]
# PSは ['1', 'AC'), ('2', 'WA')~~~]みたいな感じ

penalty = [0] * (N + 1)
AC = [False] * (N + 1)

ac = 0
for p, s in PS:
    p = int(p)
    if s == 'AC':
        if not AC[p]:
            ac += 1
            AC[p] = True
    else:
        if not AC[p]:
            penalty[p] += 1
# ここで
#penaltyは[0,0,2,1]
#ACは[0,0,1,1]みたいな感じ

penalty = [p * a for p, a in zip(penalty, AC)]
# ここでACフラグが1の所だけpenaltyを足したいが、そこでzipしてpenaltyとACの要素をひとつずつかけていくことで実現出来る。
print(ac, sum(penalty))