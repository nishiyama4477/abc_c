n, m, x = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
c = [0] * n
# おそらく習得度カウンター　n * m個になっている。言い換えれば本一つにつきm個の習得度カウンターがある。
a = [[0] * m for i in range(n)]
print("a is", a)

# おそらく本の数だけ値段を取り出している。
for i in range(n):
    c[i] = A[i][0]

#
for i in range(n):
    for j in range(m):
        print('a[i][j] is', a[i][j])
        print('A[i][j + 1] is', A[i][j + 1])
        a[i][j] = A[i][j + 1]

print('for後のaは', a)
inf = float('inf')
ans = inf

for i in range(2 ** n):
    price = 0
    comprehension = [0] * m
    for j in range(n):
        if (i >> j) & 1:
            price += c[j]
            flag = True
            for k in range(m):
                comprehension[k] += a[j][k]
                if comprehension[k] < x:
                    flag = False
            if flag:
                ans = min(ans, price)

if ans == inf:
    print(-1)
else:
    print(ans)

