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

print(ans)

solved = []
q = 0
penalties = 0
for i in ans:
    if q != int(i[0]):
        print('new problem appears!')
        penalties = 0
        q = int(i[0])
    if q != int(i[0]) and i[1] == 'WA':
        penalties += 1

    if i[1] == 'AC' and q not in solved:
        solved.append(q)

print('solved is', solved)




# corect answersの数はsolvedの長さに等しいのでlen(solved)で表せる。
print(len(solved))




