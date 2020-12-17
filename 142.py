n = int(input())

a = input().split()
list = []

for i in a:
    list.append('q')

for i, e in enumerate(a):
    list[int(e)-1] = i + 1

print(" ".join(map(str, list)))