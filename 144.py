import math, numpy
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

left = numpy.prod(list[:middle])

right = numpy.prod(list[middle:])

# print(type(middle))
# print(type(left))

point = [left, right]

result = left + right -2
print(int(result))