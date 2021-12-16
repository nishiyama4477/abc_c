# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC151
# いちよ方針。まずsolvedな問題を分ける。それからq(question)を軸にpenaltiesを足していく。qが変わればpenaltiesをリセット。

n, m = map(int, input().split())

flag = [False] * n
cnt = [0] * n

ac, wa = 0, 0

for i in range(m):
    ques, val = map(str, input().split())
    ques = int(ques)

    if not flag[ques-1]:
        if val == 'AC':
            flag[ques-1] = True
            ac += 1
        else:
            cnt[ques-1] += 1


for j in range(n):
    if flag[j]:
        wa += cnt[j]

print(ac, wa)










