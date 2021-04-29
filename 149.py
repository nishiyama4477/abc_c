# 仮説１
# 1: Xを素因数分解し、リスト化。ダブるものがあれば素数ではない
# 2: X +1しながら試していく。

X = int(input())

def prime_factorizer(z):
    list = []
    while z % 2 == 0:
        list.append(2)
        z //= 2
    f = 3
    while f * f <= z:
        if z % f == 0:
            list.append(f)
            z //= f
        else:
            f += 2
    if z != 1:
        list.append(z)
    return list

if 
while len(prime_factorizer(X)) != len(set(prime_factorizer(X))):
    X += 1
    if len(prime_factorizer(X)) == len(set(prime_factorizer(X))):
        print(X)
        break
    else:
        continue

else:
    print(X)




















