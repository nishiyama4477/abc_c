# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')


# ABC149

x = int(input())


def is_prime(n):
    flag = True
    if n > 1:
        for i in range(2, n):
            if x % i == 0:
                flag = False
                break
    if flag:
        return False
    else:
        return True


for i in range(x, 10**5+1):
    print(i)
    if is_prime(i):
        print(i)
        quit()


