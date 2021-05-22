
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')
#
# print(json.dumps(data))

a = [1,2,3,2,4,5]

print('sorted(a)[::-1]は', sorted(a)[::-1])

print('sorted(a)[0::-1]は', sorted(a)[0::-1])

b = sorted(a)[0:]
n_a = b[::-1]

print('n_aは', n_a)


# print(sorted(a)[0::-1])