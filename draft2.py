# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

l = int(input())


base = l * 10

value = base / 3

ans = value ** 3 / 1000

print(ans)