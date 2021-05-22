# import base64
#
# message = "lovecoffee"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
#
# print(base64_message)

def Pythagoras_2(k :int, m :int, n: int) -> list:
    answer = []
    answer.append(k*(m**2 - n**2))
    answer.append(2*k*m*n)
    answer.append(k*(m**2 + n**2))
    return answer

for k in range(1,5):
    for m in range(1,5):
        for n in range(1,10):
            if m <= n :
                break
            area = math.sqrt(((k+m+n)*(k+m-n)*(k-m+n)*(m+n-k))/16)

print('S={0}'.format(area))