
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
print(A)

dp = [0] * (N + 1)
dp2 = [0] * (N + 1)
cnt_w = 0
cnt_a = 0
print(dp)
print(dp2)
# dpもdp2もACの時だけ＋１される
# seq[0]は問題番号
# 2周しているforを
# ↓このループはACがあるところのdp2を1にする
for seq in A:
    if seq[1] == "AC":
        dp2[int(seq[0])] = 1
        print('dp2の' + seq[0] + 'が１になった')

# このループは初のACを1にする かつ cnt_wが分からない?????

for seq in A:
    if seq[1] == "AC" and dp[int(seq[0])] == 0:
        cnt_a += 1
        print('cnt_aが+1された')
        dp[int(seq[0])] = 1
        print('dpの' + seq[0] + 'が１になった')
    elif seq[1] == "WA" and dp[int(seq[0])] == 0 and dp2[int(seq[0])] == 1:
        cnt_w += 1
        print('cnt_wが+1された')
print(cnt_a, cnt_w)