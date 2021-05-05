# 仮説1
# itertools.permutationsを使って列挙は出来る
# 後は、列挙したものはtuple、s1はlistなのでそこを調整
import itertools

N = int(input())
s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]

# p = index, q = value(今回はtuple）
# AとBはpermutationsのindex値
A = 0
B = 0

# errorが起きた原因は、
# permutationsしたときに、かぶりがあるとか順列の問題、
# もしくは端っこの値。
if s1 == s2:
    A = 0
    B = 0
else:
    for p, q in enumerate(itertools.permutations(range(1, N + 1))):
        if list(q) == s1:
            A = p + 1
        elif list(q) == s2:
            B = p + 1

print(abs(A - B))


# 参考
# 手順：　ベースとなるlistを用意
# 　　　　index.(s1),index.(s2)でindex値を取得
# from itertools import permutaitons
#
# N = int(input())
# nlist = [i+1 for i in range(N)]
# s1 = tuple(int(x) for x in input().split())
# s2 = tuple(int(x) for x in input().split())
# S = list(permutaitons(nlist))
#
# A = S.index(s1)
# B = S.index(s2)
# print(abs(A - B))