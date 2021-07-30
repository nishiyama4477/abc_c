# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)
n, m = map(int, input().split())
Hs = [int(i) for i in input().split()]
Ms = [list(map(int, input().split())) for i in range(m)]

counter = 0

for i in range(1, len(Hs) + 1):
    li = []
    for j in Ms:
        if i in j:
            J = list(filter(lambda x: x != i, j))[0]
            if Hs[J-1] not in li:
                li.append(Hs[J-1])
    if len(li) >= 1 and max(li) < Hs[i-1] or len(li) == 0:
        counter += 1

print(counter)