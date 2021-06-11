

A, B = map(int, input().split())

x_low = (A * 100 + 7) // 8
x_high = ((A + 1) * 100 + 7) // 8 - 1
y_low = (B * 100 + 9) // 10
y_high = ((B + 1) * 100 + 9) // 10 - 1


print(x_low)
print(x_high)
print(y_low)
print(y_high)


print('\n')

print(x_low * 0.08)
print(x_high * 0.08)
print(y_low * 0.1)
print(y_high * 0.1)





# result = max(x_low, y_low)
# if result > min(x_high, y_high):
#     result = -1
# print(result)
