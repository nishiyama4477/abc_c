# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)
from collections import Counter

_count = Counter()
# print(_count)
_count.update('Welcome to Guru99 Tutorials!')
print(_count)
print('%s : %d' % ('u', _count['u']))
# print('\n')
# for char in 'Guru':
#     print('%s : %d' % (char, _count[char]))