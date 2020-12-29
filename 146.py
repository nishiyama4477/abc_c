# import math
a,b,x = map(int, input().split())

# cri = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
#
# for i in range(0, 9):
#     if a * cri[i] + b * len(str(cri[i])) <= x and a * cri[i] - 1 + b * len(str(cri[i] -1)) <= x:
#         continue
#     else:
#         r = len(str(cri[i])) -1
#         print(r)
#         break

# 値段の範囲
l = 0
r = 10**9

while r >= l:
    # if l == r:
    #     print('答えは' + str(r) + ',' + str(l))
    #     break
    dif = r - l
    mid = round((r + l) / 2)
    # print('midは' + str(mid))
    pri = a * mid + b * len(str(mid))

    if dif <= 1:
        # print('答えは' + str(r))
        print(r)
        break
    # if pri == x:
        # print(mid)
    elif pri > x:
        r = mid - 1
        # print('rは' + str(r))
    elif pri < x:
        l = mid + 1
        # print('lは' + str(l))
# else:
#     print(-1)

