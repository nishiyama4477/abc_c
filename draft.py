# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC157
# 一つ疑問があって、ある桁の予想が被ったときは−1なのか、どちらかが合っていればそれを採用するのか。
# とりまダブったら-1で実装する。
n, m = map(int, input().split())

pre = [10] * n
# print(pre)

for i in range(m):
    num = list(int(o) for o in input().split())
    if pre[num[0] - 1] == 10:
        pre[num[0] - 1] = num[1]
    # 予想がダブった時
    if pre[num[0] - 1] != 10 and num[1] != pre[num[0] - 1]:
        print(-1)
        quit()
    # ２桁以上の数で１桁目が0の時
    if n != 1 and num[0] == 1 and num[1] == 0:
        print(-1)
        quit()

# print(pre)
# ↑ここまではオッケー
# ここから下が出来ていない。0の出力とか、forで１か０かの処理をするところとか。
# あとはpreの10の部分を最小化してあげればいい。


# if pre[0] == 10:
#     pre[0] = 1
# if pre[1] == 10:
#     pre[1] = 0
# if pre[2] == 10:
#     pre[2] = 0

if n != 1:
    for i in range(n):
        if pre[i] == 10:
            if i == 0:
                print(-1)
                exit()
            pre[i] = 0


if n == 1:
    if pre == 10:
        pre = 0

ans = [str(i) for i in pre]

print(''.join(ans))
