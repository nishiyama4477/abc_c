# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC152

# 実装しないといけないポイントとして大きく二つある。
# ①: 条件にあうリスト（ここではrightとした）の最小値を取り出す。←ここでいかに早い処理を書けるか。
# ②: それらを比べてleftが常にright以下であればcount += 1、それ以外はノーカン。


n = int(input())
permutation = [int(i) for i in input().split()]


# print(permutation)

count = 0
for i, v in enumerate(permutation):
    left = v
    right = min(permutation[:i+1])
    if left == right:
        count += 1


print(count)




