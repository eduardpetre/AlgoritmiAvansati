a, b, c = list(map(int, input().split()))
n = int(input())
x = list(map(float, input().split()))

fi = [a * i**2 + b * i + c for i in x]
F = sum(fi)

pi = ["{0:.4f}".format(sum(fi[:i])/F) for i in range(n+1)]
for i in pi:
    print(i)