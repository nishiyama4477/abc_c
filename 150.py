# 仮説1
# itertools.permutationsを使って列挙は出来る
# 後は、列挙したものはtuple、s1はlistなのでそこを調整
import itertools

N = int(input())
s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]

# p = index, q = value(今回はtuple）
A = 0
B = 0

for p, q in enumerate(itertools.permutations(range(1, N + 1))):
    # print(list(q))
    if list(q) == s1:
        A = p
    elif list(q) == s2:
        B = p

print(abs(A - B))