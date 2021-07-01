# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

import math
import time

start = time.time()

print(math.gcd(3355, 2379))

time.sleep(1)

end = time.time()

print('execute is ', (end - start))

start2 = time.time()

l = (math.gcd(1,2),3)
