from itertools import product

a = "ACGT"
a = "01"

ret = list(product(a, repeat=4))

for i in ret:
    print("".join(i))