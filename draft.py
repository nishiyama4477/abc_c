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
    print(0)
    quit()

print(ans)

solved = []
q = int(ans[0][0])
print(q)

ac = 0
wa = 0

penalties = 0


for index, i in enumerate(ans):
    print('○始まるよ○')
    # 新しい問題だ！！
    if i[1] == 'WA' and q not in solved:
        print('まだ正解してないよ。だからwaを足したよ')
        penalties += 1

    if i[1] == 'AC' and q not in solved:
        print('正解した問題が追加されたよ')
        solved.append(q)
        ac += 1

    if index != len(ans) - 1 and q != int(ans[index + 1][0]):
        print('new problem appears!')
        wa += penalties
        penalties = 0
        q = int(ans[index+1][0])
        print('決算終了したよ。acは', ac, 'waは', wa, 'penaltiesは', penalties)

print('solved is', solved)




# corect answersの数はsolvedの長さに等しいのでlen(solved)で表せる。
print(len(solved))
print(wa)




