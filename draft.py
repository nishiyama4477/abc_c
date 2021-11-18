
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')

# 方針１
# N人の取り出し方それぞれに対して検証する。大きい数からやっていけば検証が通った途端にそれが答えとなる。
# import itertools

# n = int(input())
#
# testimonies = []
#
# for i in range(n):
#     a = int(input())
#     # print('A is', a)
#     x_y = []
#     for j in range(a):
#         x, y = map(int, input().split())
#         pare = [x, y]
#         x_y.append(pare)
#         # print('証言', j+1,  'は', x, y)
#     testimonies.append(x_y)
#
# print('testimonies is', testimonies)
#
# count = -float('inf')
#
# for i in range(2**n):
#     peo = []
#     for j in range(n):
#         if (i >> j) & 1:
#             peo.append(testimonies[j])
#     # ここでパターンの取得は終わっているのでそれぞれが合っているか確認。
#     # フラグとしては正直者と言われている人の発言に矛盾が生じたらアウト。矛盾とは同じ人に1と0宣言されること。
#     print('--------------------')
#     print('パターン', i, 'は', peo)
#     flag = [0] * n
#     print('flag is', flag)
#     print('正直者の数は', len(peo))
#     for k in peo:
#         print('k is', k[0])
#         # 前　嘘つき　今　正直者
#         if k[0][1] == 1 and flag[k[0][0]] < 0:
#             print('course: 1')
#             flag[k[0][0]] = 'w'
#         # 前　正直　今　嘘つき
#         elif k[0][1] == 0 and flag[k[0][0]] > 0:
#             print('course: 2')
#             flag[k[0][0]] = 'w'
#         # 正直者かつflagがwではない
#         elif k[0][1] == 1 and k[0][1] >= 0 and flag[k[0][0]] is not type(str):
#             print('course: 3')
#             flag[k[0][0]] += 10
#         # 嘘つきかつflagがwではない
#         elif k[0][1] == 0 and k[0][1] <= 0 and flag[k[0][0]] is not type(str):
#             print('course: 4')
#             flag[k[0][0]] -= 10
#         # 矛盾が発生した時（上記のifでもelifでもない時）、もしくはパターンとして正直者が1人もいない（peoの要素が0の時。
#         # これはもう少し上で場合分けしたが良さそう）の場合分けが出来ていない。
#
#     # print('flag', flag)
#     if 'w' not in flag:
#         # print('CONGRATULATION, COUNTED!!')
#         # print('___________________')
#         # print('___________________')
#         if len(peo) > count:
#             count = len(peo)
#
#
# print(count)

n = int(input())

testimonies = []

for i in range(n):
    a = int(input())
    # print('A is', a)
    x_y = []
    for j in range(a):
        x, y = map(int, input().split())
        pare = [x, y]
        x_y.append(pare)
        # print('証言', j+1,  'は', x, y)
    testimonies.append(x_y)

print('testimonies is', testimonies)
# print(len(testimonies))



for i in range(2**n):
    #peoはパターンを表す。
    peo = []
    for j in range(n):
        if (i >> j) & 1:
            peo.append(testimonies[j])
    # ここでパターンの取得は終わっているのでそれぞれが合っているか確認。
    # フラグとしては正直者と言われている人の発言に矛盾が生じたらアウト。矛盾とは同じ人に1と0宣言されること。
    print('--------------------')
    print('パターン', i, 'は', peo)
    print('要素の数は', len(peo))









