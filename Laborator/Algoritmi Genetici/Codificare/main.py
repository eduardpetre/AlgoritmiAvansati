import math

interval = list(map(float, input().split()))
a, b = interval
p = float(input())
m = int(input())

# print(a, b, p, m)

l = math.ceil(math.log(((b - a) * math.pow(10, p)), 2))
d = (b - a) / math.pow(2, l)

# print (l, d)

for _ in range(m):
    if input() == 'TO':
        x = float(input())
        nrInterval = math.floor((x - a) / d)
        nrCodificat = format(nrInterval, f'0{l}b')
        print(nrCodificat)
    else:
        x = int(input(), 2)
        nrDecodificat = a + x * d
        print('{:.{}f}'.format(nrDecodificat, l))