
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')




# 方針１
# まず、インパクトが大きいのはAの値。例えば、n = 100 のとき、1 * 100 > 1 * 3になる。
# てことは、A * ○ の値が許容範囲を超えないかでifを組める説。

###二分探索だった！！！！
# まずは昇順に並べてリストを用意


a, b, x = map(int, input().split())

# #Nは１以上なのでa+bがxよりも大きい時点でたとえ最小のInteger１が入ってきても買えない。
# if a + b > x:
#     print(0)
#     exit()
# else:

left = 1
right = 10**9

left_p = a * left + b * len(str(left))
right_p = a * right + b * len(str(right))


while left <= right:
    # left_pをそのままleftにしてしまえばいいやないか？という疑問もあるが、それは下記↓をするから出来ない。
    # print('start------------------')
    # print('-----------------------')
    # print('left is', left)
    # print('right is', right)

    mid = (left + right) // 2
    # print('mid is', mid)

    mid_p = a * mid + b * len(str(mid))
    # mid_pの次の値（next)と言う意味でn_mid_p
    n_mid_p = a * (mid + 1) + b * len(str(mid + 1))
    if mid_p == x:
        print(mid)
        exit()
    elif mid_p < x and n_mid_p > x:
        print(mid)
        exit()
    elif right - left <= 1:
        if a * right + b * len(str(right)) <= x:
            print(right)
        else:
            print(0)
        exit()
    elif mid_p < x:
        left = mid + 1
    elif mid_p > x:
        right = mid - 1
