# 仮説1: まずforループ
#      左の条件はP[:j:i]、右はPi <= Pj ← PjというのはP[:j:i]
#      P[:j:i]の全てのカズはPi以上でないといけない。　　←PiというのはP[:j:i]の最小値ということ！！！
#      今回はPiを軸として「bench」とおき、P[:j:i]をpとし、
#      min(p) < benchとなった場合はcount += 1とし、
#      print(N - count)とした。

N = int(input())
P = [int(i) for i in input().split()]

# count = 0
#
# for i, value in enumerate(P):
#     bench = P[value - 1]
#     p = P[:value]
#     if min(p) < bench:
#         count += 1
#
# print(N - count)
bench = P[0]
count = 0
for i in range(N):
    if bench >= P[i]:
        bench = P[i]
        count += 1

print(count)