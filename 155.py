# 仮説としては、　←間違い
# ①まずvalueのリストとcounterのリストを用意。
# ②counterの最大値のindex値を取り、(複数あるが、maxからのindexだと一つしか取らない。)listのindex値と照らし合わせて出力

# 仮説は間違い。Counterというmethodを使えば一発で数が分かる。）
# Counter().most_common()を使えば扱いやすい形に（dicではなくlistの中にtupleがある形
# 今回は出力結果がlexicographically orderなのでsort()した後出力した。
from collections import Counter

N = int(input())

list = []
for i in range(N):
    s = input()
    list.append(s)

counter = Counter(list).most_common()
point = counter[0][1]
result = []
for i in counter:
    if i[1] == point:
        result.append(i[0])
    else:
        break
result.sort()

for i in result:
    print(i)