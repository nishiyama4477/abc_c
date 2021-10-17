import math

N = int(input())

ans = 10 ** 12

for i in range(1, int(math.sqrt(N)) + 1):
    l = N / i
    if N % i == 0:
        ans = min(ans, i + l)

print(int(ans - 2))