# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC165
# 仮説１
# ステップを分けると、①Aのとりうる値を決める。②点数を判定し、より大きければ更新。←でも多分①の段階でおおよそのとりうる値的なのは見つけられそう。
# というより、Asからある程度数字を予測できそうな気もする。=cになるようにAを作れば良いだけ。
n, m, q = map(int, input().split())

As = []

for s in range(q):
    a = list(int(i) for i in input().split())
    As.append(a)

print(As)



