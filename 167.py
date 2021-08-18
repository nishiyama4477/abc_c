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

print(level_counter)
#####

Ns = [list(map(int, input().split())) for i in range(n)]

# ここでNsの個々の要素[list(map(int, input().split()))]とlevel_counterの要素を照らし合わせて足していく。
# 例えば、[60, 2, 2, 4]だったら、level_counter = [0, 0, 0] なので、これをlevel_counterに足すと、level_counter = [2, 2, 4]になる。
# それを繰り返していけばそれぞれのアルゴリズムに置いてXを超えそうか判定できる。
# ここでforループを使うと量が膨大になりそうだが、1 <= n, m <= 12 なので大丈夫そう。

print('n=', n)
print('m=', m)
print('x=', x)

print(Ns)

sorted_Ns = sorted(Ns)

print(sorted_Ns)


for i in Ns:
    for j, item in enumerate(i):
        if j == 0:
            continue
        else:
            level_counter[j-1] += item


print('level_counter is', level_counter)

if min(level_counter) < x:
    print(-1)
else:
    marks = [A, B, C, D, E, F, G, H, I, J, K, L] # zip時の割り当てに使う。
    for i in range(1, n+1):
        print('started')
        for j in list(combinations(sorted_Ns, i)): # jは組み合わせ ここでjの時Xを満たせるか判定したい。J is like ([60, 2, 2, 4], [70, 8, 7, 9])
            print('j is', j)

    # ここで1つ、2つ.....と取り出せる。


# ここに最安になる組み合わせを選ぶプログラムを書きたい。
# 多分方針として、組み合わせを使うと思う。値段を軸にした組み合わせを全パターンだし、１つずつ調べていき、objectiveが達成された時点でprint
# ただどうやって価格を元にパターン列挙できるか
# もしこれが成り立つなら、level_counterはいらない説。
# 列挙を考えたとして、一気に列挙するパターン（個数が１の時から複数の時まで）or combinationsを使って1つの時、2つの時、みたいにするか。
# とりま簡単なのでcombinationsでいく
# sorted()を使えば、価格に合わせて並び替えることができる。
