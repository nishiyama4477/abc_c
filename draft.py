# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC163

n = int(input())

As = [int(i) for i in input().split()]

counter = [0] * n

# print(counter)

for i in As:
    counter[i-1] += 1

for i in counter:
    print(i)





