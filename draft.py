import math

# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')
#
# print(json.dumps(data))

K = int(input())

sum = 0

for i in range(1, K+1):
    for j in range(1, K+1):
        i_j = math.gcd(i,j)
        for k in range(1, K+1):
            sum += math.gcd(i_j, k)
            sum += math.gcd(i_j, k)

print(sum)