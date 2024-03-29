# 戦略はHsを元にしてループを回しながらそれぞれをMsと照らし合わせる。
# この時、Hsの要素一つに対して、Msを全部回さないといけないのでおそらく２重のループ。

# 手順を日本語で言うと、①それぞれのobservatoryからいくつobservatoryが繋がっているか。
# ②その中で基準となるobservatoryが一番高かったor基準となるobservatoryしかないなら＋。←これを表すには、listの中の最大値maxを使うと都合が良さそう。

# 手順を振り返ると、展望台ごとにグループを作る。　それぞれのグループの中で一番高いもしくは１つだけであれば＋１。

# このプログラムは計算量がO(n*2)。これはあまり望ましくない。どう減らすか。

n, m = map(int, input().split())
Hs = [int(i) for i in input().split()]
Ms = [list(map(int, input().split())) for i in range(m)]


# print(n)
# print(m)
# print('Hs is', Hs)
# print('Ms is ', Ms)

counter = 0
# Msがindex値なのでHsを取り出す時もindex値で取り出す。
for i in range(1, len(Hs) + 1):
    # print(i, '個目', 'STARTED!!!')
    # liはライバルを貯めていくところ。
    li = []
    for j in Ms: # Msはそのままでいい。なぜならMsはindexだから。
        # print('j is', j)
        if i in j:
            # j.removeを使うと2回目の処理で使えなくなる。これが"list index out of range"の理由。
            # j.removeじゃなくてjの中のiではない方を取り出したい。そしてそれをlist.appendしたい。
            J = list(filter(lambda x: x != i, j))[0]
            # print('ライバルは', Hs[J-1])
            if Hs[J-1] not in li:
                li.append(Hs[J - 1])
    # print(Hs[i-1], 'の', 'ライバル達は is', li)
    if len(li) >= 1 and max(li) < Hs[i-1] or len(li) == 0:
        counter += 1

print(counter)



