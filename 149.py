# 仮説１
# 1: 素数判定をし、素数だったらreturn、そうでないならforループで1足しながら判定
# 2: X +1しながら試していく。
import math

X = int(input())

# 素数判定のプログラム
def prime(z):
    for i in range(2, int(math.sqrt(z)) + 1):
        if z % i == 0:
            return False
    return True

if prime(X):
    print(X)
# 素数になるまで1足しながらループを回す。
else:
    while not prime(X):
        X += 1
    else:
        print(X)










