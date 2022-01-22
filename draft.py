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
print(As)

atama = As[-1] - As[0]
ketu = k - As[-1] + As[0]


print(atama)
print(ketu)


#　円の形をした池描き、始点と終点を結んだ時の扇型の形。鋭角だと単純に始点から終点をなぞれば良い。鈍角だと真ん中から始まって終点から始点をまたぐ感じ。
# おそらく鈍角時にどの真ん中から始めるかが鍵な気がする。
if atama >= ketu:
    print('これは鋭角')
    # 鋭角の時、
else:
    print('これは鈍角')
    from_start = As[1] - As[0]
    from_end = As[-1] - As[len(As) - 2]
    if from_start >= from_end:
        print('真ん中の２番目から始点to終点')
    else:
        print('真ん中のケツから２番目から終点to始点)')







# clock = As[-1] - As[0]
# print(clock)
# unti_clock = As[0] + (k - As[-1])
# print(unti_clock)
#
# if clock <= unti_clock:
#     print('始点から時計回りにいくで')
#     print(clock)
# else:
#     print('始点から半時計回りにいくで')
#     # print(unti_clock + sum(As[1:]))
#     for i in range(len(As[1:])):
#         if i == len(As[1:]) - 1:
#             break
#         else:
#             kyori = As[i+2] - As[i+1]
#             print('kyori is', kyori)
#             unti_clock += kyori
#     print(unti_clock)





