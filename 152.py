# 仮説1: まずforループ
#      左の条件はP[:i]、右はPi <= Pj
#      P[:i]の全てのカズはPi <= Pjを満たす必要がある。
#      今回はPiを軸として「bench」とおき、P[:i]をpとし、
#      for q in pでqがbenchを下回ったときは条件に合わないと判断した。
#      全て満たせばcountを+
N = int(input())
P = [int(i) for i in input().split()]

count = 0

for i, value in enumerate(P):

    bench = P[value - 1]
    # print(value)
    p = P[:value]
    # print(p)
    # print(bench)
    # ここでpの要素全てがbench以上でなければならない

    for q in p:
        if q < bench:
            count += 1

print(N - count)