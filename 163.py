# 現段階の方針
# まずforを回しながら、BOSSが出てきたらBOSSを出現させる（もしくは最初から用意しておく）
# forでBOSSが出る度にcountしていく


n = int(input())

A = input().split()

# print(A)

# countしていくためのcounterを作る
BOSSs = [0 for i in range(1, n+1)]
# print("BOSSは", BOSSs)

# BOSSが出てきたらcounterに＋していく。
for i, v in enumerate(A):
    # print("ID", i + 2, "は")
    # print(v)
    BOSSs[int(v)-1] += 1

for q in BOSSs:
    print(q)

# print("BOSSは", BOSSs, "人")