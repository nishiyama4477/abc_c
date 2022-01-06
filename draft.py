# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC156
# 仮定①：これは与えられた数n個の平均が目的地になる。2.5などの時はおそらくどっちでもいいか、どちらか。
# なのでまずは切り捨てで作ってみる。

n = int(input())

people = list(map(int, input().split()))

place = -(-sum(people) //  len(people))

ans = 0

for i in people:
    point = (i - place) ** 2
    ans += point

print(ans)