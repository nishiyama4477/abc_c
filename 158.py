# 仮説
# ①：AとBを出す。
# ②：AとBが一緒ならそのまま出力、違う場合はどちらかに合わせてみる。
# ③：whileを使って出来そう。。。。  ×whileじゃなくて一致させないといけないので一気に同じ値にする必要がある。
import math

a, b = map(int, input().split())

# AとBは消費税抜きのそれぞれの値段
# A = a / 0.08
# B = b / 0.1

# print('Aは',A)
# print('Bは',B)

for i in range(1001):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        print(i)
        exit()

print(-1)

# より良いやり方は次回。



