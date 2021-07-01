import math

# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')
#
# print(json.dumps(data))
import math
import time



l = (math.gcd(1,2), 3)

start = time.time()

print(math.gcd(math.gcd(1,2), 3))

time.sleep(1)

end = time.time()

print(end-start)

def g(a,b):
    if b == 0:
        return a
    else:
        return g(b, a%b)

start2 = time.time()

print(g(math.gcd(1,2), 3))

time.sleep(1)

end2 = time.time()

print(end2 - start2)

