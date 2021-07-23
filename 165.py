# 仮設１は
# まず、Aは①長さNの②要素が左から右に行くにつれて大きくなる（かダブりの数含む）③M以下の数字
# そして、Q個の数字はAの得点を決める判定機
# それぞれの判定機の正誤を決めて、あっているところのcを足していったのが答え。


# まとめると
# ステップ①：まずN桁のAを見つける
# ステップ②：Q個の判定機に照らし合わせてその和が答え。

# 細かく分けると
# 列挙はだるいので、条件から遡って考える。
# 1: 条件からQ個の組み合わせを考える
# 例　Q の一個目：1~4で3になる組み合わせ　→　4-1  一般化すると　1~NでN-1になる組み合わせ　→　N-1
#  まず、上記の３を出そう→とそれはC

# 上記の一般化のコードを書ければできそう。。。。。

# 上記のQの条件に照らし合わせたA3, A1を出すコードを描きたい。
# cをターゲットとすると, Nとターゲットの差を元に組み合わせが列挙出来る。

# 犬の道をすると、difの全パターンを場合わけで作る。一応NとMの範囲は広くないので書けるが微妙。

import itertools

n, m, q = map(int, input().split())

# A = []
#
#
# for i in range(q):
#     req = [int(i) for i in input().split()]
#     print(req)
#     target = req[2]
#     print('targetは', target)
#     dif = m-target
#     print('difは', dif)
#     if dif == 1:

l = [list(map(int, input().split())) for i in range(q)]
# print("lは", l)

ran = [i for i in range(1, m+1)]
# print("ranは", ran)

As = list(itertools.combinations_with_replacement(ran, n))

# print(len(As))

X = []

for j in range(len(As)):
    c = 0
    for k in range(q):
        if As[j][l[k][1] - 1] - As[j][l[k][0] - 1] == l[k][2]:
            c += l[k][3]
    X.append(c)

print(max(X))




