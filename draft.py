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
ans = [list(input().split()) for i in range(m)]

if m == 0:
    print(0, 0)
    quit()

solved = []
wa = 0

for i in ans:
    if i[1] == 'WA' and i[0] not in solved:
        wa += 1
    if i[1] == 'AC' and i[0] not in solved:
        solved.append(i[0])

print(len(solved), wa)





