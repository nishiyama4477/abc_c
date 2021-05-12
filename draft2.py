# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

N = int(input())
p = [int(i) for i in input().split()]

print(set(p))

print(list(set(p))[:N - 2])

