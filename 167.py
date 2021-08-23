# 方針
# 縦のinputの数は本の数 = N
# 横のinputの数(C以降)はアルゴリズムの数 = M
# 例えばアルゴリズム１を達成できるか知りたいとき縦のポイントの合計がXを超えるかどうか
# つまりはstep①A11,A21....の列の合計をそれぞれ出してそれがXを上回るか、step②もし上回るのであれば、どの組み合わせが一番安く済むかを考える。
from itertools import combinations

n, m, x = map(int, input().split())

# level_counterを作る、それぞれがXを超えているか調べるリスト
level_counter = []

for i in range(m):
    level_counter.append(0)

# print(level_counter)
#####

Ns = [list(map(int, input().split())) for i in range(n)]

# ここでNsの個々の要素[list(map(int, input().split()))]とlevel_counterの要素を照らし合わせて足していく。
# 例えば、[60, 2, 2, 4]だったら、level_counter = [0, 0, 0] なので、これをlevel_counterに足すと、level_counter = [2, 2, 4]になる。
# それを繰り返していけばそれぞれのアルゴリズムに置いてXを超えそうか判定できる。
# ここでforループを使うと量が膨大になりそうだが、1 <= n, m <= 12 なので大丈夫そう。

# print('n=', n)
# print('m=', m)
# print('x=', x)
#
# print(Ns)

sorted_Ns = sorted(Ns)

# print(sorted_Ns)


for i in Ns:
    for j, item in enumerate(i):
        if j == 0:
            continue
        else:
            level_counter[j-1] += item


# print('level_counter is', level_counter)

if min(level_counter) < x:
    print(-1)
    exit()
else:
    # marks = [A, B, C, D, E, F, G, H, I, J, K, L] # zip時の割り当てに使う。
    for i in range(1, n+1):
        # print('started')
        for j in list(combinations(sorted_Ns, i)): # jは組み合わせ ここでjの時Xを満たせるか判定したい。J is like ([60, 2, 2, 4], [70, 8, 7, 9])
            if len(j) == 1:
                a = j[0]
                # 満たさなかった側
                if min(a[1:]) < x:
                    continue
                # 条件を満たした側
                else:
                    print(a[0])
                    quit()
            elif len(j) == 2:
                a = j[0]
                b = j[1]

                c = [n + o for n, o in zip(a, b)]
                if min(c[1:]) < x:
                    continue
                else:
                    print(c[0])
                    quit()

            elif len(j) == 3:
                a = j[0]
                b = j[1]
                c = j[2]

                d = [n + o + p for n, o, p in zip(a, b, c)]
                if min(d[1:]) < x:
                    continue
                else:
                    print(d[0])
                    quit()

            elif len(j) == 4:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]

                e = [n + o + p + q for n, o, p, q in zip(a, b, c, d)]
                if min(e[1:]) < x:
                    continue
                else:
                    print(e[0])
                    quit()

            elif len(j) == 5:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]

                f = [n + o + p + q + r for n, o, p, q, r in zip(a, b, c, d, e)]
                if min(f[1:]) < x:
                    continue
                else:
                    print(f[0])
                    quit()

            elif len(j) == 6:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                f = j[5]

                g = [n + o + p + q + r + s for n, o, p, q, r, s in zip(a, b, c, d, e, f)]
                if min(g[1:]) < x:
                    continue
                else:
                    print(g[0])
                    quit()

            elif len(j) == 7:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                f = j[5]
                g = j[6]

                h = [n + o + p + q + r + s + t for n, o, p, q, r, s, t in zip(a, b, c, d, e, f, g)]
                if min(h[1:]) < x:
                    continue
                else:
                    print(h[0])
                    quit()


            elif len(j) == 8:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                f = j[5]
                g = j[6]
                h = j[7]


                i = [n + o + p + q + r + s + t + u for n, o, p, q, r, s, t, u in zip(a, b, c, d, e, f, g, h)]
                if min(i[1:]) < x:
                    continue
                else:
                    print(i[0])
                    quit()


            elif len(j) == 9:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                f = j[5]
                g = j[6]
                h = j[7]
                i = j[8]

                js = [n + o + p + q + r + s + t + u + v for n, o, p, q, r, s, t, u, v in zip(a, b, c, d, e, f, g, h, i)]
                if min(js[1:]) < x:
                    continue
                else:
                    print(js[0])
                    quit()


            elif len(j) == 10:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                f = j[5]
                g = j[6]
                h = j[7]
                i = j[8]
                js = j[9]

                k = [n + o + p + q + r + s + t + u + v + w for n, o, p, q, r,s ,t, u, v, w in zip(a, b, c, d, e, f, g, h, i, js)]
                if min(k[1:]) < x:
                    continue
                else:
                    print(k[0])
                    quit()



            elif len(j) == 11:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                f = j[5]
                g = j[6]
                h = j[7]
                i = j[8]
                js = j[9]
                k = j[10]

                l = [n + o + p + q + r + s + t + u + v + w + x for n, o, p, q, r, s, t, u, v, w, x in zip(a, b, c, d, e, f, g, h, i, js, k)]
                if min(l[1:]) < x:
                    continue
                else:
                    print(l[0])
                    quit()


            elif len(j) == 12:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                f = j[5]
                g = j[6]
                h = j[7]
                i = j[8]
                js = j[9]
                k = j[10]
                l = j[11]

                m = [n + o + p + q + r + s + t + u + v + w + x + y for n, o, p, q, r, s, t, u, v, w, x, y in zip(a, b, c, d, e, f, g, h, i, js, k, l)]
                if min(m[1:]) < x:
                    continue
                else:
                    print(m[0])
                    quit()



print(-1)


    # ここで1つ、2つ.....と取り出せる。


# ここに最安になる組み合わせを選ぶプログラムを書きたい。
# 多分方針として、組み合わせを使うと思う。値段を軸にした組み合わせを全パターンだし、１つずつ調べていき、objectiveが達成された時点でprint
# ただどうやって価格を元にパターン列挙できるか
# もしこれが成り立つなら、level_counterはいらない説。
# 列挙を考えたとして、一気に列挙するパターン（個数が１の時から複数の時まで）or combinationsを使って1つの時、2つの時、みたいにするか。
# とりま簡単なのでcombinationsでいく
# sorted()を使えば、価格に合わせて並び替えることができる。
