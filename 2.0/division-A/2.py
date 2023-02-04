import math


def vec_angle(v1, v2):
    w1, w2 = v1
    u1, u2 = v2
    return math.atan2(w2 * u1 - w1 * u2, w1 * u1 + w2 * u2)


def sign(x):
    if x < 0:
        return 1
    return 0


def is_parallel(points):
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    x3, y3 = points[3]
    vec1 = (x1 - x0, y1 - y0)
    vec2 = (x2 - x0, y2 - y0)
    vec3 = (x3 - x0, y3 - y0)
    angle12 = vec_angle(vec1, vec2)
    angle13 = vec_angle(vec1, vec3)
    order = [0, 2, 1, 3]
    if sign(angle12) == sign(angle13):
        if abs(angle12) < abs(angle13):
            order = [0, 1, 2, 3]
        else:
            order = [0, 1, 3, 2]
    order = [points[j] for j in order]
    if order[1][0] - order[0][0] == order[2][0] - order[3][0] and \
            order[1][1] - order[0][1] == order[2][1] - order[3][1]:
        return True
    return False


def main(lst):
    for el in lst:
        if is_parallel(el):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    _n = int(input())
    _lst = []
    for i in range(_n):
        sp = list(map(int, input().split()))
        _lst.append([(sp[j], sp[j + 1]) for j in range(0, 8, 2)])
    main(_lst)
