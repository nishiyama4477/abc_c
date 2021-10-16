li = [1,2,3,4,5]
li2 = [6,7,8,9,10]


zip_list = zip(li, li2)

sum = [x + y for x, y in zip_list]

print(sum)