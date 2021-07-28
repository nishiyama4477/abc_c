# 戦略はHsを元にしてループを回しながらそれぞれをMsと照らし合わせる。
# この時、Hsの要素一つに対して、Msを全部回さないといけないのでおそらく２重のループ。

# 手順を日本語で言うと、①それぞれのobservatoryからいくつobservatoryが繋がっているか。
# ②その中で基準となるobservatoryが一番高かったor基準となるobservatoryしかないなら＋。

# 今起きているエラー(list index out of range)は、iとjでループの回数が違うからだと思う。←肌感レベルだから信憑性はない。

n, m = map(int, input().split())
Hs = [int(i) for i in input().split()]
Ms = [list(map(int, input().split())) for i in range(m)]


print(n)
print(m)
print('Hs is', Hs)
print('Ms is ', Ms)

counter = 0
# Msがindex値なのでHsを取り出す時もindex値で取り出す。
for i in range(1, len(Hs) + 1):
    print(i, '個目', 'STARTED!!!')
    for j in Ms: # Msはそのままでいい。なぜならMsはindexだから。
        print('j is', j)
        if i in j:
            j.remove(i)
            J = j[0] # このJはどちらが高いかの比較対象(いわばライバル。)のindex
            print('Hs[i-1] is', Hs[i-1], '基準')
            print('Hs[J-1] is', Hs[J-1], 'ライバル')
            if Hs[i-1] <= Hs[J-1]:
                # もしライバルに高さで負けたらbreakして次の基準にバトンタッチ。
                break
            elif j == Ms[m-1]:
                counter += 1
            else:
                continue

#
print(counter)



