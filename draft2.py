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

n = int(input())

for i in range(1, n):
  base = n-1
