# 仮説
# ①：AとBを出す。
# ②：AとBが一緒ならそのまま出力、違う場合はどちらかに合わせてみる。
# ③：whileを使って出来そう。。。。  小さい方を大きい方に合わせるのか、その逆なのか、それとも片方だけでいいのか
import math

a, b = map(int, input().split())

A = a / 0.08
B = b / 0.1

if A > B:
    new_B = B
    while new_B <= A:
        new_B = math.floor(new_B * 0.1)
        if new_B == A:
            B = new_B
            break
        new_B += 1

if B > A:
    new_A = A
    while new_A <= B:
        new_A = math.floor(new_A * 0.08)
        if new_A == B:
            A = new_A
            break
        new_A += 1

if A == B:
    print(A)
else:
    print(-1)