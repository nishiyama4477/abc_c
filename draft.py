
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')
import math
import itertools

n = int(input())

li = [input().split() for i in range(n)]

fac = list(itertools.permutations(li))

print('それぞれの点は', li)

# print('組み合わせは', fac)

print('組み合わせのサンプルは', fac[0])


total = 0

for j in fac:
# ひとつのパターンを使ったパターン
    sample_sum = 0
    for i, val in enumerate(j):
        if i == len(j)- 1:
            break
        else:
            val = list(int(i) for i in val)
            val2 = list(int(i) for i in j[i + 1])
            print(val)
            print(val2)

            zipped = zip(val, val2)
            s = [x+y for x, y in zipped]
            print('sum は', s)
            ans = math.sqrt(sum([i**2 for i in s]))
            print('ans　は', ans)
            sample_sum += ans
    total += sample_sum


print(total / len(fac))






# # ひとつのパターンを使ったパターン
# sample_sum = 0
# for i, val in enumerate(fac[0]):
#     if i == len(fac[0])- 1:
#         break
#     else:
#         val = list(int(i) for i in val)
#         val2 = list(int(i) for i in fac[0][i + 1])
#         print(val)
#         print(val2)
#
#         zipped = zip(val, val2)
#         s = [x+y for x, y in zipped]
#         print('sum は', s)
#         ans = math.sqrt(sum([i**2 for i in s]))
#         print('ans　は', ans)
#         sample_sum += ans
# print(sample_sum)