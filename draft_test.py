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

sample = ([50, 2, 3, 9],)

sample2 = ([60, 2, 2, 4], [70, 8, 7, 9])

sample3 = ([50, 2, 3, 9], [60, 2, 2, 4], [70, 8, 7, 9])

# 出したい結果はsample2だったら[10, 9, 13]みたいな感じ。


print(len(sample))
# jが一つの時
if len(sample) == 1:
    a = sample[0][1:]
    print(a)

print(len(sample2))
# jが2つの時
if len(sample2) == 2:
    a = sample2[0][1:]
    b = sample2[1][1:]

    c = [n + o for n, o in zip(a, b)]

    print(c)

print(len(sample3))
# jが3つの時
if len(sample3) == 3:
    a = sample3[0][1:]
    b = sample3[1][1:]
    c = sample3[2][1:]

    d = [n + o + p for n, o, p in zip(a, b, c)]

    print(d)



a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = [x + y + z for x, y, z in zip(a, b, c)]

# print(d)


