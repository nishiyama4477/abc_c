# 1問目
base = [1,0,5]
for i in range(1, 31):
    if i < 4:
        pass
    else:
        ans = sum(base[i - 4:])
        base.append(ans)

print(base[-1])


# 2問目
def cal(n):
    list = []
    i = 1
    while i*i <= n:
        if n % i == 0 and i <= 5000000:
            list.append(i)
            if i != n // i and i <= 5000000:
                list.append(n//i)
        i += 1
    return sum(list)

print(cal(1234567890))

# print(sum(cal(1234567890)))

# 3問目

# 4問目
import math

count = 0

a = 1
while a <= 100:
    b = a
    while b <= 10000/ a:
        if math.sqrt(a*a + b*b).is_integer():
            count += 1
    b += 1
a += 1

print(count)
