# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

list = [1,2,3,4,5]

for i, v in enumerate(list):
    print(v, 'だお')
    for s, q in enumerate(list[i + 1:]):
        print('sは', s)
        print('qは', q)
        # print(list[i:])
        # print(abs(list[i] - list[s + 1]))
