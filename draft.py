# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC152
n = int(input())
permutation = [int(i) for i in input().split()]


count = 0
for i in range(1, n+1):
    left = permutation[i-1]
    right = min(permutation[:i])
    if left == right:
        count += 1
    else:
        continue
    # print('left is', left)
    # print('right is', right)

print(count)







