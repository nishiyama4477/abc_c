# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC155
# ①１番多く登場したやつを探す。
# ②それをlexicographicalに出力する。
# TLEを防ぐにはたぶんforループ一回で済まさないといけない。

n = int(input())

words = []
counter = []

for i in range(n):
    # print('ループ', i+1, '回目')
    word = input()
    if word not in words:
        words.append(word)
        counter.append(1)
    else:
        where = words.index(word)
        counter[where] += 1

    # print('現時点でのwords', words)
    # print('現時点でのcounter', counter)


# print(words)
# print(counter)

# zipped = list(zip(words, counter))
#
# print(zipped)
#
# zipped2 = sorted(zipped)
#
# print(zipped2)
#
# most = sorted(counter, reverse=True)[0]

sample_list = sorted(list(zip(counter, words)), reverse=True)
# print(sample_list)

most = list(sample_list[0])[0]
answer = []

for i, v in sample_list:
    if i == most:
        answer.append(v)
    else:
        break

answer.sort()

for i in answer:
    print(i)