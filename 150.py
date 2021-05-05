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
        # print(list(q))
        if list(q) == s1:
            # print('s1は', s1)
            # print('qは', list(q))
            A = p + 1
            # print('Aは', A)
        elif list(q) == s2:
            # print('s2は', s2)
            # print('qは', list(q))
            B = p + 1
            # print('Bは', B)

print(abs(A - B))