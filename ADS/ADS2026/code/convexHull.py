import matplotlib.pyplot as plt
import random
import math
import time

def random_points(n, max_coord):
    l = [[random.randint(0,max_coord), random.randint(0,max_coord)] for i in range(n)]
    return l

def filter_in_square(points):
    '''find the quadrangle whose vertices are the extreme points in direction
nort-east, north-west, south-west, south-east and returns only poits that
are not inside the quadrangle'''
    ne_bound =  points[0][0] + points[0][1]
    nw_bound = -points[0][0] + points[0][1]
    sw_bound = -points[0][0] - points[0][1]
    se_bound =  points[0][0] - points[0][1]
    ne = points[0]
    nw = points[0]
    sw = points[0]
    se = points[0]
    for p in points:
        if  p[0] + p[1] > ne_bound:
            ne_bound = p[0] + p[1]
            ne = p
        if -p[0] + p[1] > nw_bound:
            nw_bound = -p[0] + p[1]
            nw = p
        if -p[0] - p[1] > sw_bound:
            sw_bound = -p[0] - p[1]
            sw = p
        if  p[0] - p[1] > se_bound:
            se_bound = p[0] - p[1]
            se = p
    print("four corners:", ne, nw, sw, se)
    outer = []
    for p in points:
        if p == nw or p == ne or p == se or p == sw or counter_clock(nw, ne, p) or counter_clock(ne, se, p) or counter_clock(se, sw, p) or counter_clock(sw, nw, p):
            outer.append(p)
    return outer
    
def counter_clock(a, b, c):
    det = a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - a[1]*b[0] - b[1]*c[0] - c[1]*a[0]
    return det > 0

def graham_scan(p):
    fig, ax = plt.subplots(2, 2)
    ax[0][0].scatter([x[0] for x in p], [x[1] for x in p])
    p = filter_in_square(p)
    ax[0][1].scatter([x[0] for x in p], [x[1] for x in p], color = "black")
    v = sorted(p)
    p_left = v[0]
    for i in range(1, len(v)):
        v[i].insert(0, (v[i][1]-p_left[1])/(v[i][0]-p_left[0]))
    v[0].insert(0, -float("inf"))
    v.sort(reverse = True)
    ax[1][0].scatter([x[1] for x in v], [x[2] for x in v], color = "black")
    ax[1][1].scatter([x[1] for x in v], [x[2] for x in v], color = "black")
    ax[1][0].plot([x[1] for x in v] + [v[0][1]], [x[2] for x in v] + [v[0][2]], color = "green")
    ax[1][1].plot([x[1] for x in v] + [v[0][1]], [x[2] for x in v] + [v[0][2]], color = "green")
    v = [[x[1], x[2]] for x in v]
    i = 0
    while i < len(v) - 2:
        if counter_clock(v[i], v[i+1], v[i+2]):
            v.pop(i+1)
            if i > 0:
                i -= 1
        else:
            i += 1
    ax[1][1].scatter([x[0] for x in v], [x[1] for x in v], color = "red")
    ax[1][1].plot([x[0] for x in v] + [v[0][0]], [x[1] for x in v] + [v[0][1]], color = "black")
    plt.show()
    return v
    
if __name__ == "__main__":
    p = random_points(100, 10000)
    c_h = graham_scan(p)


        