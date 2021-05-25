# 仮説としては、
# ①まずvalueのリストとcounterのリストを用意。
# ②counterの最大値のindex値を取り、(複数あるが、maxからのindexだと一つしか取らない。)listのindex値と照らし合わせて出力

N = int(input())

list = []
counter = []

for i in range(N):
    s = input()
    if s not in set(list):
        list.append(s)
        counter.append(1)
        print(list)
        print(counter)
    else:
        print('count up!')
        counter[list.index(s)] += 1
        print(list)
        print(counter)

max_value = max(counter)

get_list = []
for i in counter:
    if i == max_value:
        get_list.append(counter.index(i))

print(get_list)

