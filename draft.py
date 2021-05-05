from itertools import permutations
from pprint import pprint

list = list(permutations(range(1,5)))
pprint(list)

P = (2,1,3,4)
Q = (1,2,4,3)

Pi = list.index(P) + 1
Qi = list.index(Q) + 1

# print(Pi)
# print(Qi)

print(abs(Pi - Qi))
