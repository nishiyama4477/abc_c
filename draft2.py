# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)
# i = 2
# j = [1,2]
# p = [5,6,7]
# j.remove(i)
# print(j)
# print(j[0])

# aではない数（２）を取り出したい。
a = 1
li = [1, 2]
b = list(filter(lambda x: x == a, li))


print(type(li))
print(li)
print(b)

q = []

print(len(q))
