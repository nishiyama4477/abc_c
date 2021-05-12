# 仮説1: まず、jを見つける
# 　　　　①条件の左側を用意。　例　Pi <= Pj のPi  *どっちでもいいとは思う。
#      　②(1 <= j <= i)の範囲を定義、の内でひとつづづ判定していく。
# 考察：　順番どうりに並んだpと、そのままのpがいる　→ そのままのリストをenumerateで取れれば、よくないか？
N = int(input())
p = [int(i) for i in input().split()]

# i == 順番どうり並んだp  I == p
count = 0
for i, I in enumerate(p):
    if I in list(set(p))[N - 3:]:
        pass
    else:
        left = p[I + 1]
        right = max(p[:I - 1])
        if right >= left:
            count += 1

print(count)
