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
        # print(list)
        # print(counter)
    else:
        print('count up!')
        counter[list.index(s)] += 1
        # print(list)
        # print(counter)

# print('結果は', list)
# print('結果は', counter)
zipped = set(zip(list, counter))
# print(zipped)

max_value = max(counter)

for i in zipped:
    if i[1] == max_value:
        print(i[0])



# print(set(zipped).get('bet'))





