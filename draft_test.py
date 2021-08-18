# n = int(input())
# Ns = [list(map(int, input().split())) for i in range(n)]
#
# print(Ns)

from itertools import combinations

# sortedと仮定
li2 = [[100, 3, 7, 5, 3, 1], [164, 4, 5, 2, 7, 8], [334, 7, 2, 7, 2, 9]]

t = list(combinations(li2, 2))

# print(t)
#
# for i in t:
#     print(i)

x = 10
sample = ([60, 2, 2, 4], [70, 8, 7, 9])

for i in sample:
    print(i)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = [x + y + z for x, y, z in zip(a, b, c)]

print(d)

