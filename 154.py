N = int(input())

list = list(map(int, input().split()))

n_list = set(list)

if len(list) != len(n_list):
    print(('NO'))
else:
    print('YES')