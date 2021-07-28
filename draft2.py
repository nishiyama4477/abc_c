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

for i in range(1,4):
    print(i, 'iだよ')
    for j in range(1,3):
        if j == 2:
            break
        else:
            print(j)


