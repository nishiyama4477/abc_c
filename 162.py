# import itertools

# ステップ1：列挙しないといけない
# ステップ2：3ペアから2ペアに直しつつ足していく → gcd(a, gcd(b,c))
# ポイント:多分被りが有る。例えば1,2,3と2,1,3。これをどう処理するか→もし全列挙するならsort()を使えばいい！
# またsortしたリストはuniqueで無ければならない。
# maybe I can use 'enum' library ????? NO!! we can use itertoolsのどれか!!
# 今回の問題は組み合わせの重複有り!!順列の重複有りや無しではない。
# ポイントはitertoolsのどれを使うか。もしかしたら2重に掛けているのかも知れない

### TLEを解決するために
# ①itertools.productは重複がある。例えば(1,2,1)と(2,1,1)←この考え方は間違っている。重複を外してしまうとそのときの値が取れなくなる。
# ②改善の余地があるのは 1:itertoolsの列挙の部分なのか 2:forでcountしていくところなのか←上記の理由から1は現在微妙。

### ヒントを見ると、2桁の数が決まった後に（(gcd(a,b),c)のように）ユークリッドの互除法を使うと計算が少なくてすむらしい、、、
### つまり、①；gcd(gcd(a,b))よりも②：(gcd(a,b),c)をユークリッドの互除法を使う方が早いらしい、、、
### またこれら時間の違いを調べる為に時間を計測するプログラムが書けると便利そう、、、


# total = 0
# for i in list(itertools.product(range(1,k+1), repeat=3)):
#     count = math.gcd(i[0], math.gcd(i[1], i[2]))
#     total += count
#
# print(total)

import math

K = int(input())

sum = 0

for i in range(1, K+1):
    for j in range(1, K+1):
        i_j = math.gcd(i,j)
        for k in range(1, K+1):
            sum += math.gcd(i_j, k)

print(sum)


