
# import json
# import base64
#
# data = {}
# with open('https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')




# 方針１
# まず、インパクトが大きいのはAの値。例えば、n = 100 のとき、1 * 100 > 1 * 3になる。
# てことは、A * ○ の値が許容範囲を超えないかでifを組める説。

a, b, x = map(int, input().split())

#Nは１以上なのでa+bがxよりも大きい時点でたとえ最小のInteger１が入ってきても買えない。
if a + b > x:
    print(0)
    exit()
else:
