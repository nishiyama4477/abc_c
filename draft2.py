# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

N, M, Q = map(int, input().split())
l = [list(map(int, input().split())) for l in range(Q)]

import itertools

t = [i for i in range(1, M + 1)]
# ここでゆうAは、問題文のAで数自体はいindex値を表している。
A = list(itertools.combinations_with_replacement(t, N))
print(t)
print(l, 'と', A)
X = []
for j in range(len(A)): # ここでAの全パターンについて検証していく。そのために、Aのindex値としてjをとる。
  c = 0
  for k in range(Q):
    if A[j][l[k][1] - 1] - A[j][l[k][0] - 1] == l[k][2]: # 　これはAのbi - Aのai = cを表している。
      c += l[k][3]
  X.append(c)
print(X)
print(max(X))