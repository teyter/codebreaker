from math import floor
from time import time
start = time()

def printlist(lst):
    for i in lst:
        print(i)
def string(lst):
    return ''.join(map(str,lst))

# Time Complexity: O( len(a)^k * k )
def bruteforce(k,a):
    b = [i for i in range(k-1,-1,-1)]
    ret = []
    base = len(a)
    sic = base**k
    for i in range(sic):
        s = []
        for j in range(k):
            x = floor(i/base**b[j]) % base 
            s.append(a[x])
        s = string(s)
        ret.append(s)
    print(len(ret))
    return ret

def test(a,k):
    ret = []
    for i in range(a**k):
        ret.append("ACGT")
    return ret
lower_case = []
upper_case = []
numeric = []
for c in map(chr, range(97, 123)):
    lower_case.append(c)
for c in map(chr, range(65, 91)):
    upper_case.append(c)
for c in map(chr, range(48, 58)):
    numeric.append(c)

test(62,5)
alphabet = lower_case + upper_case + numeric
a = "ACGT"
#(bruteforce(4,alphabet))
end = time()
print(end-start)

