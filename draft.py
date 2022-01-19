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

clock = As[-1] - As[0]
print(clock)
unti_clock = As[0] + (k - As[-1])
print(unti_clock)

if clock <= unti_clock:
    print('始点から時計回りにいくで')
    print(clock)
else:
    print('始点から半時計回りにいくで')
    # print(unti_clock + sum(As[1:]))
    for i in range(len(As[1:])):
        if i == len(As[1:]) - 1:
            break
        else:
            kyori = As[i+2] - As[i+1]
            print('kyori is', kyori)
            unti_clock += kyori
    print(unti_clock)




# distances = []
#
# for i in range(len(As)):
#     if i == len(As) - 1:
#         v = As[i]
#         # print('v is', v)
#         dif = abs(k - v)
#         # print('dif is', dif)
#         distances.append(dif)
#     else:
#         v = As[i]
#         v2 = As[i+1]
#         dif = abs(v - v2)
#         distances.append(dif)
#
# # print('distances is', distances)
#
# a = list(combinations(distances, 2))
#
# # print('組み合わせは', a)
#
# a_sum = list(sum(i) for i in a)
#
# # print('それぞれ距離は', a_sum)
#
# a_sum.sort()
#
# print(a_sum[0])

# print(min(a_sum))




