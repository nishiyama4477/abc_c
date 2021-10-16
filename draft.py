
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


length = len(p)

# ans = float('inf')
if len(p) == 1:
    print(n - 1)
else:
    ans = p[0] + reduce(mul, p[1:])


    for ind, i in enumerate(p):
        if len(p) != length:
            p.append(p[ind-1])
        # print('軸は', i)
        p.remove(i)

        for j in range(1, len(p)):
            rival_num = len(p) - j
            # print('相手の数は', rival_num)
            combinations = itertools.combinations(p, rival_num)
            # print('その選び方は', list(combinations))
            rival_li = [reduce(mul, i) for i in combinations]
            # print('敵は', rival_li )# 上のコードをコメントアウトしないと正しいアウトプットにならない。
            my_li = [n // i for i in rival_li]
            # print('味方は', my_li)
            move = [x + y for x, y in zip(rival_li, my_li)]
            maybe_ans = min(move)
            if maybe_ans <= ans:
                ans = maybe_ans

    print(ans-2)

# 1748670


