# 仮説1
# itertools.permutationsを使って列挙は出来る
# 後は、列挙したものはtuple、s1はlistなのでそこを調整
import itertools

N = int(input())
s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]

# p = index
A = 0
B = 0
print("s1は", s1)
print("s2は", s2)
for p, q in enumerate(itertools.permutations(range(N))):
    print("pは" , p)
    print("qは", q)
    # if q == s1:
    #     A = p
    # elif q == s2:
    #     B = p
print(A)
print(B)