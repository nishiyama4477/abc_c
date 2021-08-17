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

n, m = map(int, input().split())
Hs = [int(i) for i in input().split()]
Ms = [list(map(int, input().split())) for i in range(m)]

Ms_mid = len(Ms)//2

Ms_1half = Ms[:Ms_mid]
Ms_2half = Ms[Ms_mid + 1:]

print(Ms_1half)
print(Ms_2half)

for p in range(1, len(Hs) // 2 + 1):
    print('①Hs is', Hs[p-1])
    # for s in Ms

for q in range(len(Hs)//2 + 1, len(Hs) + 1):
    print('Hs is', Hs[q-1])



# with ThreadPoolExecutor(max_workers=2) as executor:
#     a = executor.submit(wait_on_b)
#     b = executor.submit(wait_on_a)


