# 1.

# n = int(input())
# test = []
# for i in range(n):
#     xp, yp, xq, yq, xr, yr = map(int, input().split())
#     test.append((xp, yp, xq, yq, xr, yr))
#
# for i in range(n):
#     xp = test[i][0]
#     yp = test[i][1]
#
#     xq = test[i][2]
#     yq = test[i][3]
#
#     xr = test[i][4]
#     yr = test[i][5]
#
#     det = 1 * xq * yr + xp * yq * 1 + 1 * xr * yp - 1 * xq * yp - xr * yq * 1 - 1 * xp * yr
#
#     if det > 0:
#         print("LEFT")
#     elif det < 0:
#         print("RIGHT")
#     elif det == 0:
#         print ("TOUCH")

# ----------------------------------------------------

# 2.

# n = int(input())
# pct = []
# for i in range(n):
#     x, y = map(int, input().split())
#     pct.append((x, y))
#
# left = 0
# right = 0
# straight = 0
#
# for i in range(1, n):
#     a = pct[i-1]
#     b = pct[i]
#     c = pct[(i+1)%n]
#
#     dir = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
#
#     if dir > 0:
#         left += 1
#     elif dir < 0:
#         right += 1
#     else:
#         straight += 1
#
# print(left, right, straight)

# -------------------------------------------------

# 3.

# def orientation(a, b, c):
#     return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
#
# def createList (points):
#     list = [points[0], points[1]]
#
#     for i in range(2, len(points)):
#         list.append(points[i])
#
#         while len(list) > 2 and orientation(list[-3], list[-2], list[-1]) <= 0:
#             list.pop(-2)
#
#     return list
#
# n = int(input())
# points = []
#
# for i in range(n):
#     x, y = map(int, input().split())
#     points.append((x, y))
#
# points = sorted(points)
# listinf = createList(points)
#
# points.reverse()
# listsup = createList(points)
#
# list = listinf[1:] + listsup[1:]
# print(len(list))
# for point in list:
#     print(point[0], point[1])