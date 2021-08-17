# n = int(input())
# Ns = [list(map(int, input().split())) for i in range(n)]
#
# print(Ns)

from itertools import combinations

li = [1,2,3,4,5]

s = combinations(li, 2)

# print(list(s))

li2 = [[100, 3, 7, 5, 3, 1], [164, 4, 5, 2, 7, 8], [334, 7, 2, 7, 2, 9]]

t = list(combinations(li2, 2))

# print(t)

for i in t:
    print(i)