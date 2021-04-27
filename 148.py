a, b = map(int, input().split())
import math

G = math.gcd(a, b)

L = (a * b) // G

print(L)