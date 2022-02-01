# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC162
# 仮説１：取り出すlistを作ってあげて、そこからitertoolsで取り出す。
# 解法はユークリッドの互除法を使うことだった！！
# とりまgcdを使った後残りの２数に対してユークリッドしてみようと思う。
import math

k = int(input())

sum = 0

for i in range(1,k+1):
    for j in range(1, k+1):
        i_j = math.gcd(i,j)
        for l in range(1, k+1):
            num = math.gcd(i_j, l)
            sum += num

print(sum)






