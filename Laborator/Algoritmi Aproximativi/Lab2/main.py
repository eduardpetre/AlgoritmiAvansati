# # 1.
# Determinant
def orientation(p, q, r):
    det = (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])
    return det


# Cautare binara a punctului din query
def bin_search(points, point):
    l = 0
    r = len(points) - 1
    while l <= r:
        m = (l + r) // 2
        turn = orientation(points[0], points[m], point)
        if turn > 0:
            l = m + 1
        elif turn < 0:
            r = m - 1
        else:
            return m
    return r


def relative_pos(points, point):
    i = bin_search(points, point)

    # print(i, points[i], points[(i + 1) % n], point)

    if i == 0 or i == len(points)-1:
        return -1

    turn1 = orientation(points[i - 1], points[i], point)
    turn2 = orientation(points[i], points[(i + 1) % n], point)

    if turn1 > 0 and turn2 > 0:
        return 1
    elif turn1 < 0 and turn2 < 0:
        return -1
    elif turn1 == 0 and turn2 >= 0:
        return 0
    elif turn1 > 0 and turn2 == 0:
        return 0
    else:
        return -1

n = int(input())
points = []
dict = {}
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    dict[(x, y)] = 1

m = int(input())
query = []
for i in range(m):
    x, y = map(int, input().split())
    query.append((x, y))

for x in query:
    if x in dict.keys():
        print("BOUNDARY")
    else:
        pos = relative_pos(points, x)

        if pos == 1:
            print("INSIDE")
        elif pos == 0:
            print("BOUNDARY")
        elif pos == -1:
            print("OUTSIDE")


# -----------------------------------------------------

# 2.

# verifica daca punctul point se afla pe dreapta determinata de p1 p2
def onEdge(point, p1, p2):
    prod = (p1[0] - point[0]) * (p2[1] - point[1]) - (p1[1] - point[1]) * (p2[0] - point[0])
    # daca produsul e 0 atunci punctul nu se afla pe dreapta
    if prod != 0:
        return 0
    # se verifica daca punctele p1 p2 se afla pe dreapta paralela cu axa OX
    # si se verifica daca coord x a punctului point se afla intre coord x a lui p1 si p2
    if p1[0] != p2[0]:
        return ((p1[0] <= point[0] <= p2[0]) or (p1[0] >= point[0] >= p2[0]))
    # analog daca punctele p1 p2 se afla pe dreapta paralela cu axa OY
    return ((p1[1] <= point[1] <= p2[1]) or (p1[1] >= point[1] >= p2[1]))


# verifica daca dreapta care trece prin point paralela cu OY intersecteaza poligonul
def intersect(point, p1, p2):
    # verifica daca p1 si p2 se afla ambele sub sau deasupra dreptei
    if point[1] > p1[1] and point[1] > p2[1] or point[1] <= p1[1] and point[1] <= p2[1]:
        return 0
    # calculeaza coordonata oriziontala a punctului de intersectie
    # si verifica daca este mai mare decat coordonata x a punctului point
    # adica daca intersectia se afla la dreapta dreptei determinate de point paralela cu OY
    else:
        x_intersect = ((point[1] - p1[1]) * (p2[0] - p1[0]) + p1[0] * (p2[1] - p1[1])) / (p2[1] - p1[1])
        return x_intersect > point[0]


def relative_pos(point, polygon):
    count = 0
    for i in range(len(polygon) - 1):
        p1 = polygon[i]
        p2 = polygon[i + 1]

        if onEdge(point, p1, p2):
            return 0

        if intersect(point, p1, p2):
            count += 1

    if onEdge(point, polygon[len(polygon) - 1], polygon[0]):
        return 0

    p1 = polygon[len(polygon) - 1]
    p2 = polygon[0]
    if intersect(point, p1, p2):
        count += 1

    if count % 2:
        return 1
    else:
        return -1


# definirea poligonului
n = int(input())
polygon = []
for i in range(n):
    x, y = map(int, input().split())
    polygon.append((x, y))

# testarea punctelor
m = int(input())
query = []
for i in range(m):
    x, y = map(int, input().split())
    query.append((x, y))

for point in query:
    location = relative_pos(point, polygon)
    if location == 1:
        print("INSIDE")
    elif location == 0:
        print("BOUNDARY")
    else:
        print("OUTSIDE")


# ---------------------------------------------------------

# 3.

def monotone(axis):
    # se cauta punctul cu cea mai mica valoare pe axa x respectiv y
    mini = float('inf')
    pos = 0
    for i in range(n):
        if axis == 'x':
            if points[i][0] < mini:
                mini = points[i][0]
                pos = i
        else:
            if points[i][1] < mini:
                mini = points[i][1]
                pos = i

    if axis == 'x':
        miniPoint = points[pos][0]
    else:
        miniPoint = points[pos][1]

    ok = True

    # se parcurg toate punctele 2 cate 2
    # se verifica ca atunci cand se gaseste un punct cu o coordonata mai mica,
    # sa nu se gaseasca alta mai mare
    # adica sensul sa se schimbe o singura data
    for i in range(1, n):
        j = (pos + i) % n
        if axis == 'x':
            point = points[j][0]
        else:
            point = points[j][1]

        if point < miniPoint:
            ok = False

        if point > miniPoint and not ok:
            return False

        miniPoint = point

    return True


n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

if monotone('x'):
    print('YES')
else:
    print('NO')

if monotone('y'):
    print('YES')
else:
    print('NO')
