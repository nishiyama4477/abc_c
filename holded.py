n = int(input())

testimonies = []

for i in range(n):
    a = int(input())
    # print('A is', a)
    x_y = []
    for j in range(a):
        x, y = map(int, input().split())
        pare = [x, y]
        x_y.append(pare)
        # print('証言', j+1,  'は', x, y)
    testimonies.append(x_y)

print('testimonies is', testimonies)
print(len(testimonies))

for i in range(2**n):
    #peoはパターンを表す。
    peo = []
    for j in range(n):
        if (i >> j) & 1:
            peo.append(testimonies[j])
    # ここでパターンの取得は終わっているのでそれぞれが合っているか確認。
    # フラグとしては正直者と言われている人の発言に矛盾が生じたらアウト。矛盾とは同じ人に1と0宣言されること。
    print('--------------------')
    print('パターン', i, 'は', peo)
    print('要素の数は', len(peo))
    for a in peo:
        print(a)


