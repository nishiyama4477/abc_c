# ABC155　解答

import collections

n = int(input())
s = []
for i in range(n):
    s.append(input())

# print(n)
# print(s)


c = collections.Counter(s)
c_s = c.most_common()
m = c.most_common()[0][1]

print(c)
print(c_s)
print(m)


ans = []
for j in range(len(c_s)):
    if c_s[j][1] != m:
        break
    else:
        ans.append(c_s[j][0])

print('ans is', ans)
ans.sort()
for t in ans:
    print(t)
