# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

# このプログラムの上手さの一つは一見１の時の処理が抜けているように思うがsumで監理している。
# このプログラムは3段階でsumを足している
# またk=3の時はforを2つ通る

import math
K=int(input()) # K=2,3,4 gcdを求める回数=2^3、3^3、4^4
sum=0
for i in range(1,K+1):  #(n,n,n)
  sum+=i
print('とりまsumは',sum)

# k = 2の時
if K>1:  #(n,n,m),(n,m,m)
  print('course1')
  print('★1回目のループ', K-1, '回まわるよ')
  for j in range(1,K): # k=2の時ループは1回しか回らない    K=3の時ループは2回回る
    print('●1回目のループ', j, '回目')
    # print('j=',j)
    print('☆2回目のループ', K-j,'回まわるよ')
    for q in range(j + 1, K + 1): # k=2の時ループは1回しか回らない  K=3の時ループは1回目(j=1)に1回と2回目(j=2)に2回回る。
      print('〇2回目のループ', q-1, '回目')
      # print('q=', q)
      sum+= math.gcd(j, q) * 6  # なぜ６なの？？？ j=2, K=3である

print('cource1のsumは', sum)

print('-----------------')
print('-----------------')
x = sum
# k >= 3の時
if K>2:  #(n,m,l)
  print('course2')

  print('★1回目のループ', K-2, '回まわるよ')
  for s in range(1,K-1): # k=3の時1回しか回らない s=1
    print('●1回目のループ', s, '回目')
    print('☆2回目のループ', K-s-1, '回まわるよ')
    for t in range(s+1,K): # k=3の時1回しか回らない t=2
      print('〇2回目のループ', t-1, '回目') # ←怪しい

      print('三回目のループ', K-t, '回まわるよ')
      for u in range(t+1,K+1): # k=3の時1回しか回らない u=3
        print('三回目のループ', u-2, '回目') # ←怪しい
        sum+=math.gcd(math.gcd(s,t),u)*6   # math.gcd(math.gcd(1,2),3) * 6

print('cource2のsumは',sum-x)

print(sum)