lst = [2,3,5]

n = 6
while len(lst) < 10001:
    b = True
    for i in lst:
        if n % i == 0:
            b = False
            break
    if b:
        lst.append(n)
    n += 1

print(lst[-1])