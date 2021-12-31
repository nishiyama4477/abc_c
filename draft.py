# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC155

n = int(input())

words = []
counter = []

for i in range(n):
    word = input()
    if word not in words:
        words.append(word)
        counter.append(1)
    else:
        where = words.index(word)
        counter[where] += 1

# print(words)
# print(counter)

zipped = list(zip(words, counter))

zipped2 = sorted(zipped)

most = sorted(counter, reverse=True)[0]

for value, key in zipped2:
    if key == most:
        print(value)