l = int(input())
C1 = format(int(input(), 2), f'0{l}b')
C2 = format(int(input(), 2), f'0{l}b')
i = int(input())

c1 = C1[:i] + C2[i:]
c2 = C2[:i] + C1[i:]

print(c1)
print(c2)
