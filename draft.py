import itertools
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')

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

print(prime_factorizer(n))

# 素因数分解された後のlistの過半数の組み合わせを取り出し、その組み合わせを掛け合わしたもの
# で一番数が小さくなるやつがx軸（もしくはy軸）になる.
# 例えば112は[2,2,2,2,7]なので片方は3つ。3つの組み合わせの中で一番小さくなるのは222=8なので
# 答えは8, 14(2*7）になる、、、、はず、、、
combinations = itertools.combinations(prime_factorizer(n), -(-len(prime_factorizer(n)) // 2))

for i in combinations:
    selected =