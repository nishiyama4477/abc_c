# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

import math

a, b = map(int, input().split())

# AとBは消費税抜きのそれぞれの値段
A = a / 0.08
B = b / 0.1

print(A)
print(B)

if A == B:
    print(A)
elif A != B:
    if A < B:
        # Aを変えてBに寄せたとき
        A = B
        print('Aは', A)
        print('Bは', B)
        if math.floor(A * 0.08) == a:
            print('route1')
            print(B)
    # Bを変えてAに寄せたとき
    elif A > B:
        B = A
        print('Aは', A)
        print('Bは', B)
        if math.floor(B * 0.1) == b:
            print('route2')
            print(A)
else:
    print('失敗')


# AとBをイコールにしないといけない


# print(math.floor(B * 0.08))
# print(math.floor(A * 0.1))