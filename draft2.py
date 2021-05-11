# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)
import sys
from pprint import pprint

# input = sys.stdin.readline
# N,M= map(int,input().split())
# PS= [input().strip().split() for i in range(M)]

a = [1,2,3]
b = ['a', 'b', 'c']

zipped = zip(a,b)
print(zipped)
