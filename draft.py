
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

N, M = map(int, input().split())
A = []
if M == 0:
    print(0, 0)
    sys.exit()
else:
    for _ in range(M):
        a, b = input().split()
        A.append([a, b])


# dp1とは,その問題においてＡＣが「決算」されたかを表す。ＡＣのフラグ
dp = [0] * (N + 1)
# dp2とは,「ＡＣがある問題のフラグ」の列
dp2 = [0] * (N + 1)
cnt_w = 0
cnt_a = 0

# dpもdp2もACの時だけ＋１される
# seq[0]は問題番号
# 2周しているforを
# ↓このループはACがあるところのdp2を1にする
# 定義として、ACがある問題だけが「決算」の対象となる。ここでは対象となる問題を割り出す。
for seq in A:
    if seq[1] == "AC":
        dp2[int(seq[0])] = 1

# このループはその問題において初のACを足す。その問題において、ACが存在しない、つまり、dp2が[0]であればcnt_wはされない。

for seq in A:
    if seq[1] == "AC" and dp[int(seq[0])] == 0:
        cnt_a += 1
        dp[int(seq[0])] = 1
    elif seq[1] == "WA" and dp[int(seq[0])] == 0 and dp2[int(seq[0])] == 1:
        cnt_w += 1
print(cnt_a, cnt_w)