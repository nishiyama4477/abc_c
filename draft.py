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
# 仮定②：上手くいかなかったので仮定二つ目。for rangeで数直線一つずつみる方法。予想はTLE。

n = int(input())

people = list(map(int, input().split()))
# print('people is', people)

# このplace決めが違う可能性が高い。
# place = -(-sum(people) // len(people))
# print('place is', place)
#
# # ここから下はおそらく間違っていない。
#
# ans = 0
#
# for i in people:
#     point = (i - place) ** 2
#     ans += point
#
# print(ans)
ans = float('inf')

for place in range(1, max(people)+1):
    # print('place is', place)
    points = 0
    for j in people:
        # print('人は', j)
        p = (j - place) ** 2
        points += p
    if points <= ans:
        ans = points

print(ans)