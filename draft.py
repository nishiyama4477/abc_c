
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


from operator import mul
from functools import reduce
import itertools

n = int(input())

def prime_factorizer(num):
    li = []
    while num % 2 == 0:
        li.append(2)
        num //= 2
    base = 3
    while base * base <= num:
        if num % base == 0:
            li.append(base)
            num //= base
        else:
            base += 2

    if num != 1:
        li.append(num)
    return li

p = prime_factorizer(n)
print('pは', p)

base = float('inf')

#pを左からスライスする方式に変えた
for i, value in enumerate(p):
    if i == len(p) - 1:
        break
    left = p[:i+1]
    right = p[i+1:]
    # print('left is', left)
    # print('right is', right)
    l_num = reduce(mul, left)
    r_num = reduce(mul, right)
    # print('l_num is', l_num)
    # print('r_num is', r_num)
    dis = l_num + r_num
    if dis <= base:
        base = dis

print('base is', base)

# ここでエラー。このpが空っぽなので。つまり、素因数分解した時に要素が一つしかないパターン。
if len(p) == 1:
    print(n - 1)
else:
    print(base - 2)

length = len(p)

for ind, i in enumerate(p):
    if len(p) != length:
        p.append(p[ind-1])
    print('軸は', i)
    p.remove(i)

    for j in range(1, len(p)):
        rival_num = len(p) - j
        print('相手の数は', rival_num)
        combinations = itertools.combinations(p, rival_num)
        print('その選び方は', list(combinations))
        print('その選び方は', [reduce(mul, i) for i in combinations])# 上のコードをコメントアウトしないと正しいアウトプットにならない。


# 1748670


