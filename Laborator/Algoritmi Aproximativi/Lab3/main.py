# 1.

# def determinant(xD, yD):
#     det = xA * (yB * ((xC ** 2 + yC ** 2) * 1 - 1 * (xD ** 2 + yD ** 2)) - (xB ** 2 + yB ** 2) * (yC * 1 - 1 * yD) + 1 * (yC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * yD)) \
#           - yA * (xB * ((xC ** 2 + yC ** 2) * 1 - 1 * (xD ** 2 + yD ** 2)) - (xB ** 2 + yB ** 2) * (xC * 1 - 1 * xD) + 1 * (xC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * xD)) \
#           + (xA ** 2 + yA ** 2) * (xB * (yC * 1 - 1 * yD) - yB * (xC * 1 - 1 * xD) + 1 * (xC * yD - yC * xD)) \
#           - 1 * (xB * (yC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * yD) - yB * (xC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * xD) + (xB ** 2 + yB ** 2) * (xC * yD - yC * xD))
#
#     return det
#
# xA, yA = map(int, input().split())
# xB, yB = map(int, input().split())
# xC, yC = map(int, input().split())
#
# n = int(input())
# for i in range(n):
#     xD, yD = map(int, input().split())
#     det = determinant(xD, yD)
#     if det == 0:
#         print("BOUNDARY")
#     elif det > 0:
#         print("INSIDE")
#     else:
#         print("OUTSIDE")

# 2.

# def determinant(xA, yA, xB, yB, xC, yC, xD, yD):
#     det = xA * (yB * ((xC ** 2 + yC ** 2) * 1 - 1 * (xD ** 2 + yD ** 2)) - (xB ** 2 + yB ** 2) * (yC * 1 - 1 * yD) + 1 * (yC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * yD)) \
#           - yA * (xB * ((xC ** 2 + yC ** 2) * 1 - 1 * (xD ** 2 + yD ** 2)) - (xB ** 2 + yB ** 2) * (xC * 1 - 1 * xD) + 1 * (xC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * xD)) \
#           + (xA ** 2 + yA ** 2) * (xB * (yC * 1 - 1 * yD) - yB * (xC * 1 - 1 * xD) + 1 * (xC * yD - yC * xD)) \
#           - 1 * (xB * (yC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * yD) - yB * (xC * (xD ** 2 + yD ** 2) - (xC ** 2 + yC ** 2) * xD) + (xB ** 2 + yB ** 2) * (xC * yD - yC * xD))
#
#     return det
#
# xA, yA = map(int, input().split())
# xB, yB = map(int, input().split())
# xC, yC = map(int, input().split())
# xD, yD = map(int, input().split())
#
# detAC = determinant(xA, yA, xB, yB, xC, yC, xD, yD)
# if (detAC > 0):
#     print("AC: ILLEGAL")
# else:
#     print("AC: LEGAL")
#
#
# detBD = determinant(xB, yB, xC, yC, xD, yD, xA, yA)
# if (detBD > 0):
#     print("BD: ILLEGAL")
# else:
#     print("BD: LEGAL")

# 3.

# x_min, x_max, y_min, y_max = float('-inf'), float('inf'), float('-inf'), float('inf')
# n = int(input())
# for i in range(n):
#     a, b, c = map(int, input().split())
#     if a != 0:
#         x = -c/a
#         if a < 0:
#             x_min = max(x_min, x)
#         else:
#             x_max = min(x_max, x)
#     if b != 0:
#         y = -c/b
#         if b < 0:
#             y_min = max(y_min, y)
#         else:
#             y_max = min(y_max, y)
#
# # print(x_min, x_max, y_min, y_max)
#
# if x_min > x_max or y_min > y_max:
#     print("VOID")
# elif x_min == float('-inf') or x_max == float('inf') or \
#         y_min == float('-inf') or y_max == float('inf'):
#     print("UNBOUNDED")
# else:
#     print("BOUNDED")


# 4.
def intersectie(plane, xP, yP):
    x_min, x_max, y_min, y_max = float('-inf'), float('inf'), float('-inf'), float('inf')
    for i in range(len(plane)):
        a, b, c = plane[i]

        # print(a, b, c)
        # print(xP, yP)

        # daca punctul nu apartine planului
        if not(a != 0 and a * xP + c < 0 or b != 0 and b * yP + c < 0):
            continue

        if a != 0:
            x = -c / a
            if x < xP:
                x_min = max(x_min, x)
            else:
                x_max = min(x_max, x)

        if b != 0:
            y = -c / b
            if y < yP:
                y_min = max(y_min, y)
            else:
                y_max = min(y_max, y)

    # print(x_min, x_max, y_min, y_max)

    if x_min > x_max or y_min > y_max or \
            x_min == float('-inf') or x_max == float('inf') or \
            y_min == float('-inf') or y_max == float('inf'):
        return -1
    else:
        area = (x_max-x_min) * (y_max-y_min)
        return area

n = int(input())
plane = []
for i in range(n):
    a, b, c = map(int, input().split())
    plane.append([a, b, c])

m = int(input())
for i in range(m):
    x, y = map(float, input().split())

    area = intersectie(plane, x, y)
    if (area == -1):
        print("NO")
    else:
        print("YES")
        print(area)
