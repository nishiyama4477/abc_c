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
print('sumは',sum)
# k = 2の時
if K>1:  #(n,n,m),(n,m,m)
  print('course1')
  for j in range(1,K): # k=2の時ループは1回しか回らない    K=3の時ループは2回回る
    for k in range(j+1,K+1): # k=2の時ループは1回しか回らない  K=3の時ループは1回目(j=1)に1回と2回目(j=2)に2回回る。
      sum+=math.gcd(j,k)*6  # なぜ６なの？？？ j=2, K=3である

print('sumは', sum)
# k >= 3の時
if K>2:  #(n,m,l)
  print('course2')
  for s in range(1,K-1): # k=3の時1回しか回らない s=1
    for t in range(s+1,K): # k=3の時1回しか回らない t=2
      for u in range(t+1,K+1): # k=3の時1回しか回らない u=3
        sum+=math.gcd(math.gcd(s,t),u)*6   # math.gcd(math.gcd(1,2),3) * 6
print(sum)