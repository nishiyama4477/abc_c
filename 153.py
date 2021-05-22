n, k = map(int,input().split())
H = list(map(int, input().split()))

# print('Hは', H)


## set じゃダブった奴が消えてしまう
if len(H) >= k:
    # print('1')
    new_H = sorted(H)[::-1]
    # print('new_Hは',new_H)
    print(sum(new_H[k:]))
else:
    # print('2')
    print(0)