"""
AB = 28
zz = 702
A = 1
"""

def Name2Number(name):

    name = reversed(name)
    sum = 0
    for i, c in enumerate(name):
        sum += (ord(c) - 64) * (26 ** i)
    return sum

print(Name2Number("AB"))