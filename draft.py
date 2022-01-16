# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC159
# 仮説①：Lをいかにして３桁の掛け算にするか、それらを掛け合わせて出来る数を最大化させる。
# ポイントは３で割り切れない数がきた時。


l = int(input())

l3 = l // 3
# actl3 = l / 3

# print(l3)
# print(actl3)

print(l3**3)
# print(actl3**3)