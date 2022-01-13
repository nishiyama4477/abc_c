# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC158
# 仮説①：forで回す。が、範囲は最小から最大まで決められるはず。例えば、a=2、b=2のとき、
# 最小はx = 2.9999 / 0.08、最大はx = 2/0.1 の時。この範囲に消費税10%があれあ出力する。
# ポイントは四捨五入ではなく切り捨て。　
import math
a, b = map(int, input().split())

mi8 = a / 0.08
ma8 = (a + 1) / 0.08

print('mi8 is', mi8)
print('ma8 is', ma8)

mi10 = a / 0.10
ma10 = (a + 1) / 0.10

print('mi10 is', mi10)
print('ma10 is', ma10)

for i in range(int(mi10), int(ma10) + 1):
    if math.floor(i * 0.08) == b:
        print(i)
        exit()


