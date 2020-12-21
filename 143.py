n = int(input())
s = input()

count = 1

for i, slime in enumerate(s):
    if i == len(s) -1:
        break
    if slime != s[i+1]:
        count += 1

print(count)