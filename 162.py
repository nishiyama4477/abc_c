import math
import itertools

k = int(input())

# ステップ1：列挙しないといけない
# ステップ2：3ペアから2ペアに直しつつ足していく → gcd(a, gcd(b,c))
# ポイント:多分被りが有る。例えば1,2,3と2,1,3。これをどう処理するか→もし全列挙するならsort()を使えばいい！
# またsortしたリストはuniqueで無ければならない。
# maybe I can use 'enum' library ????? NO!! we can use itertoolsのどれか!!
# 今回の問題は組み合わせの重複有り!!順列の重複有りや無しではない。
# ポイントはitertoolsのどれを使うか。もしかしたら2重に掛けているのかも知れない

l = list(itertools.permutations(range(1,k+1),3))
print(l)
#
# total = 0
# for i in l:
#     count = math.gcd(i[0], math.gcd(i[1], i[2]))
#     total += count
#
# print(total)