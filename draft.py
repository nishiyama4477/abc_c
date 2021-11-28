# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC148
# A_primesとB_primesのconcatenateするときのポイントとして、二つに共通する因数は消去して良い。片方にしかない因数は消去してはならない。
import math
from operator import mul
from functools import reduce


def prime_fact(n):
    p_numbers = []
    while n % 2 == 0:
        p_numbers.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)+1), 2):
        while n % i == 0:
            p_numbers.append(i)
            n = n // i
    if n > 2:
        p_numbers.append(n)

    return p_numbers


a, b = map(int, input().split())

A_primes = prime_fact(a)
B_primes = prime_fact(b)

# print('A_primes is', A_primes)
# print('B_primes is', B_primes)
#
# print(prime_fact(18696))

uncommon = set(A_primes) ^ set(B_primes)

for i in A_primes:
    if i in uncommon:
        B_primes.append(i)


# print(B_primes)

print(reduce(mul, B_primes))

