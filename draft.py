# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC160
# 仮説1：①隣り合う数の差をforで出し、それをlistにappendする。②listからlen(As)-1個取り出す組み合わせの中で最小のモノが答え。
# ←これをsortで並び替えてスライスする方法に切り替える！！

# 円の周りをどう回るか。回り方は２種類しかなくて、上半分か下半分か。それを決めるときの分かれ目は二つある。
# ①どこから始めるか②右回りか左回りか

from itertools import combinations

k, n = map(int, input().split())
As = list(int(i) for i in input().split())
# print(As)

#　円の形をした池描き、始点と終点を結んだ時の扇型の形。鋭角だと単純に始点から終点をなぞれば良い。鈍角だと真ん中から始まって終点から始点をまたぐ感じ。
# おそらく鈍角時にどの真ん中から始めるかが鍵な気がする
# 上のは間違い。なぜなら、始点と終点は変わるから。ベストな始点と終点の組み合わせが鋭角か鈍角か。強いて言うならね。でも鋭角と鈍角の考え方自体がおかしい説。
# 仮説２：まずn個の家の隣あう家同士の距離が一番遠い２軒を見つける。それらの家が始点と終点。
# それらでリストをスライスして、短い方をなぞるようにclockwiseかanticlockwiseかを決める。


dis = []

most_dis = -float('inf')

for i in range(len(As)):
    if i == len(As) - 1:
        to = As[i]
        frm = As[0]
        kyori = k - to + frm
        dis.append(kyori)
        if most_dis <= kyori:
            most_dis = kyori
            left = frm
            right = to
        break
    to = As[i+1]
    frm = As[i]
    kyori = to - frm
    dis.append(kyori)
    if most_dis <= kyori:
        most_dis = kyori
        left = frm
        right = to

# print('dis is', dis)
# print('most_dis is', most_dis)

dis.remove(most_dis)

print(sum(dis))
# # leftとrightは始点と終点候補
# print('left is', left)
# print('right is', right)
#
# # leftの原点との距離をs、rightの右端との距離をtとおく。と、s = left、t = k - right
# s = left
# t = k - right
#
# if s>=t:
#