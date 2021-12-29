# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC153
n, special = map(int, input().split())

monsters = list(int(i) for i in input().split())

# print('n is', n)
# print('special is', special)
# print('monsters is', monsters)

if n <= special:
    print (0)
    exit()

monsters.sort(reverse=True)

# print('sorted monsters is', monsters)

left_monsters = monsters[special:]

# print(left_monsters)

print(sum(left_monsters))
