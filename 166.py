# 戦略はHsを元にしてループを回しながらそれぞれをMsと照らし合わせる。
# この時、Hsの要素一つに対して、Msを全部回さないといけないのでおそらく２重のループ。

n, m = map(int, input().split())
Hs = [int(i) for i in input().split()]
Ms = [list(map(int, input().split())) for i in range(m)]


print(n)
print(m)
print('Hs is', Hs)
print('Ms is ', Ms)

counter = 0

for i in range(1, len(Hs) + 1):
    print(i, '回目', 'STARTED!!!')
    print('i is ', i)
    for j in Ms:
        print('j is', j)
        if i in j:
            j.remove(i)
            J = j[0]
            print('J is', J)
            print('Hs[i-1] is', Hs[i-1])
            print('Hs[J-1] is', Hs[J-1])
            if Hs[i-1] > Hs[J-1]:
                counter += 1
                print('プラスされたよ！')
        #     print('q is', q)
        # print('j is', j)
        # print('Hs[i] is', Hs[i])

print(counter)



