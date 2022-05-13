import math


def circle_area(r_a):
    # circle
    if type(r_a) != int and type(r_a) != float:
        float(r_a)



    r = float(r_a)
    r *= r
    r *= math.pi
    return r


def rectangle_area(l_a, w_a):
    # rectangle


    l = float(l_a)
    w = float(w_a)
    a = w * l
    return a


def square_area(l_a):
    # square
    l = float(l_a)
    return l * l


def triangle_area(b_a, h_a):
    # triangle


    b = float(b_a)
    h = float(h_a)
    a = b * h
    a /= 2
    return a

