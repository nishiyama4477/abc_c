
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')

import itertools
from operator import mul
from functools import reduce

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
# print(p)

# 素因数分解された後のlistの過半数の組み合わせを取り出し、その組み合わせを掛け合わしたもの
# で一番数が小さくなるやつがx軸（もしくはy軸）になる.
# 例えば112は[2,2,2,2,7]なので片方は3つ。3つの組み合わせの中で一番小さくなるのは222=8なので
# 答えは8, 14(2*7）になる、、、、はず、、、
combinations = list(itertools.combinations(prime_factorizer(n), -(-len(prime_factorizer(n)) // 2)))

# print('過半数は', -(-len(prime_factorizer(n)) // 2))

# leastは掛け合わせた時の最小の組み合わせ。掛け算はする前で[2,2,3]みたいな状態。
least = combinations[0]

# print('combinationsは,', combinations)
# print('最初のcombinationsは', least)

for i in combinations:
    selected = reduce(mul, i)
    if selected < reduce(mul, least):
        # print('更新されたお')
        least = i

# print('leastは', least)

for i in least:
    p.remove(i)

# print('removeされたpは', p)

# ここでエラー。このpが空っぽなので。つまり、素因数分解した時に要素が一つしかないパターン。
if not p:
    print(n - 1)
else:
    print(reduce(mul, least) + reduce(mul, p) - 2)

