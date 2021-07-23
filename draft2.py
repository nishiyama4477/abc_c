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
# tというのは、Mのrange、つまりAのそれぞれの桁のとりうる値。
print('tは', t)
# lというのは、Qのこと。
print('lは', l)
# Aというのは、そのままAの列挙。
print('Aは', A)
X = []
for j in range(len(A)): # ここでAの全パターンについて検証していく。そのために、Aのindex値としてjをとる。
  print('検証開始！')
  print('jは', j)
  c = 0
  for k in range(Q): # それぞれのAに対してQつ分の条件について検証していく。
    print('kは', k)
    if A[j][l[k][1] - 1] - A[j][l[k][0] - 1] == l[k][2]: # 　これはAのbi - Aのai = cを表している。
      # 少しややこしいが、Aは3数の列挙。
      # A[j]は1 2 3。
      # [l[k][1] - 1]はQのkつ目の2つ目。つまり、例題１でいうところの3をindex値3-2を使って取り出そうとしている。.
      # A[j][l[k][1] - 1]はAのindex値2。
      c += l[k][3]
  X.append(c)
print('Xは', X)
# Xというのは可能性のあるAそれぞれの得点。
print(max(X))