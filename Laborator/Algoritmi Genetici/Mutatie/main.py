l, k = list(map(int, input().split()))
C = list(format(int(input(), 2), f'0{l}b'))
p = list(map(int, input().split()))

pFiltered = [p[i] for i in range(k) if p.count(p[i])%2 != 0 and not p[i] in p[:i]]

for i in pFiltered:
    if C[i] == '0':
        C[i] = '1'
    else:
        C[i] = '0'

print(''.join(C))
