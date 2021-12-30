# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC154
n = int(input())

numbers = list(i for i in map(int, input().split()))


answers = set(numbers)

if len(numbers) == len(answers):
    print('YES')
else:
    print('NO')
