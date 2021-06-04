# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)
N, M = map(int, input().split())

t = [-1] * N

for _ in range(M):
    s, c = map(int, input().split())
    s -= 1
    # 条件が二つ以上有るときつまり、①t[s]に先客がいる　かつ　②新規のｃである
    if t[s] != -1 and t[s] != c:
        print(-1)
        exit()
    t[s] = c


# 2～3桁の場合は先頭が0だとダメ
if N != 1:
    if t[0] == 0:
        print(-1)
        exit()

    if t[0] == -1:
        t[0] = 1

# 先頭以外で値が決まっていないものは0にする
    for i in range(1, N):
        if t[i] == -1:
            t[i] = 0

# 1桁の場合、入らなくても0のままいける。
else:
    if t[0] == -1:
        t[0] = 0
#
print(t)
# print(''.join(map(str, t)))