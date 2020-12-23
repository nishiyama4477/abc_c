import math
n = int(input())

list = []

while n % 2 ==0:
    list.append(2)
    n /= 2

for i in range(3, int(n + 1), 2):
    if n % i == 0:
        list.append(i)
        n /= i

if n > 2:
    list.append(int(n))

middle = math.ceil(len(list) / 2)

def mul_each(each):
    result = 1
    for i in each:
        result = i * result

    return result

left = mul_each(list[:middle])

right = mul_each(list[middle:])

# print(type(middle))
# print(type(left))
# print(list)
# print(right)
# print(left)
point = [left, right]

result = left + right -2
print(int(result))