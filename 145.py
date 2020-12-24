import math, itertools
n = int(input())
all_town = []
for i in range(n):
    town = [int(i) for i in input().split()]
    all_town.append(town)

all_towns = list(itertools.permutations(all_town))

distances = []
for each_town in all_towns:
    each_dis = []
    for i in range(0, len(each_town) - 1):
        left = (each_town[i][0] - each_town[i + 1][0]) ** 2
        right = (each_town[i][1] - each_town[i + 1][1]) ** 2
        result = math.sqrt(left + right)
        each_dis.append(result)

    distances.append(sum(each_dis))

print(sum(distances) / len(all_towns))

# そもそも階乗文あるパターンはfor文では無理。
# ↓2つの町の間の距離の計算
# left = (all_town[i][0] - all_town[i + 1][0]) ** 2
# right = (all_town[i][1] - all_town[i + 1][1]) ** 2
# result = math.sqrt(left + right)


# ルートごとにforループを回す。
# each_town = ([0,1], [0,0], [1,0])
# each_dis = []
# for i in range(0, len(each_town) - 1):
#         left = (each_town[i][0] - each_town[i + 1][0]) ** 2
#         right = (each_town[i][1] - each_town[i + 1][1]) ** 2
#         result = math.sqrt(left + right)
#         each_dis.append(result)
#
# print(sum(each_dis))
#
# each_town = ([1,0], [0,1], [0,0])
# each_dis = []
# for i in range(0, len(each_town) - 1):
#         left = (each_town[i][0] - each_town[i + 1][0]) ** 2
#         right = (each_town[i][1] - each_town[i + 1][1]) ** 2
#         result = math.sqrt(left + right)
#         each_dis.append(result)
#
# print(sum(each_dis))

# 階乗とはn(n-1)(n-2)で求められる。


