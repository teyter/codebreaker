from math import sqrt

lst = [2,3,5]

n = 7
while len(lst) < 10001:
    b = True
    for i in lst:
        sqr = int(sqrt(n)) + 1
        if i > sqr:
            break
        if n % i == 0:
            b = False
            break
    if b:
        lst.append(n)
    n += 2

print(lst[-1])