n, m, x = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
c = [0] * n
# おそらく習得度カウンター　n * m個になっている。言い換えれば本一つにつきm個の習得度カウンターがある。
a = [[0] * m for i in range(n)]
print("a is", a)

# おそらく本の数だけ値段を取り出している。
for i in range(n):
    c[i] = A[i][0]

#　ここでそれぞれの習熟度をlistとして出す
for i in range(n):
    for j in range(m):
        print('a[i][j] is', a[i][j])
        print('A[i][j + 1] is', A[i][j + 1])
        a[i][j] = A[i][j + 1]

print('for後のaは', a)
print('ちなみにcは', c)
# ここまでにある材料はそれぞれの経験値のリスト(a = [2, 2, 4], [8, 7, 9], [2, 3, 9]])とn, m, xとc(c = [価格のリスト])

# とりまひと段落

print('--------------')
print('--------------')

# ここのinfは「圧倒的に小さい値」「圧倒的に大きい値」を意味し、comparisonに使われる。ここでは＋のinfなので「圧倒的に大きい値」を意味し、
# valuesの中で一番小さい値を見つけるために使われていると推測する。
inf = float('inf')
# ここのansは最小になってほしい値。
ans = inf


# n, m, x, a（経験値集めたやつ）, c（価格集めたやつ）が使われる。ここでaとcは下の作業で値を輸入するために使われる、輸入元みたいなイメージ
print('2 ** n is', 2 ** n)

counter = 0
flag_false = 0

for i in range(2 ** n): # ?????なぜ2乗なのか分からない。自分の仮説はiを使いたかったから。→答えは「ある集合Aの要素がnの時、集合Aの部分集合はnの２乗になる」から
    print('START！')
    print('i is', i)
    price = 0
    comprehension = [0] * m # comprehensionは経験値分のリスト
    print('comprehension is', comprehension)
    for j in range(n):
        print('j is',  bin(j))
        if (i >> j) & 1: # ??????この条件文も分からない。→　これはフラグチェックをしているだけ。ぶどう•みかん•りんごの例を見たら分かるが、もしjシフトした時それが１であればその果物(ぶどうかみかんかりんご）は存在することになる。
            print('条件に当てはまったよ！この時iとjは', i, 'と', j)
            counter += 1
            price += c[j]
            flag = True
            # ↓このループは経験値を足していくループ
            for k in range(m):
                comprehension[k] += a[j][k] # j個目の本のk個目の経験値i
                if comprehension[k] < x:
                    flag = False
            # 経験値を足し終わった後にflag=True（つまり基準を満たせばansに値が入る。）ここで前回入ってきたpriceとの比較を行い、値の小さな方が採用される。
            if flag:
                ans = min(ans, price)
            else:
                flag_false += 1

print('counter is', counter)
print('flag_false is', flag_false)
# 値が見つからなかったケース,
# ansは無限大の＋なのでpriceに値が入った時点でansはpriceになるはず。
if ans == inf:
    print(-1)
else:
    print(ans)

