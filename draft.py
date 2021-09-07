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

# お試しで一回ThreadPoolExecutorを使ってやってみる！！

from concurrent.futures import ThreadPoolExecutor

# list = [4,10,1]
# def bit_plus(list):
#   sum = 0
#   for bit in range(1<<len(list)): # 0(0b000)から7(0b111)まで
#     for i in range(len(list)):
#       mask = 1 << i
#       print('mask is', mask)
#       print('bit is', bin(bit))
#       if bit&mask: # 右からi番目にビットが立っているかどうか判定
#         sum += list[i]
#   return sum
# print(bit_plus(list))

for i in range(7, 16):
  print(i, 'の binは', bin(i))


