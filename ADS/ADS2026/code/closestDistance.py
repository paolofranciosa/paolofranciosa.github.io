import random
import math
import time

def random_points(n, dim, m):
    '''return a list of n points in a space in dim dimensions.
Each point is a list of dim numbers in [0, m]'''
    p = []
    for i in range(n):
        p.append(random_point(dim, m))
    return p

def random_point(dim, m):
    return [random.randint(0, m) for i in range(dim)]

def distance(p1, p2):
    diff_2_sum = sum(((p1[i]-p2[i])**2 for i in range(len(p1))))
    return math.sqrt(diff_2_sum)

def compute_delta(pts):
    '''determines a random point p in pts and returns the smallest distance between p and points in pts'''
    pos = random.randint(0, len(pts)-1)
    return min([distance(pts[pos], pts[i]) for i in range(len(pts)) if i != pos])
    
def closest_distance(points):
#    print(f'closest_distance called on {len(points)} points')
    if len(points[0]) != 2:
        print("only works for 2 dimensions")
        exit(0)
    
    if len(points) < 15:
        return brute_closest_distance(points)
    
    delta = compute_delta(points)
    min_x = min((points[i][0] for i in range(len(points))))
    max_x = max((points[i][0] for i in range(len(points))))
    min_y = min((points[i][1] for i in range(len(points))))
    max_y = max((points[i][1] for i in range(len(points))))
#    print(min_x, max_x, min_y, max_y)
    if max_x - min_x > max_y - min_y:
        if max_x - min_x < delta * 3:
            return brute_closest_distance(points)
        max_x_1 = (max_x + min_x)/2 + delta/2
        min_x_2 = (max_x + min_x)/2 - delta/2
        points_1 = [points[i] for i in range(len(points))
                                    if points[i][0] <= max_x_1
                    ]
        points_2 = [points[i] for i in range(len(points))
                                    if min_x_2 <= points[i][0]
                    ]
    else:
        if max_y - min_y < delta * 3:
            return brute_closest_distance(points)
        max_y_1 = (max_y + min_y)/2 + delta/2
        min_y_2 = (max_y + min_y)/2 - delta/2
        points_1 = [points[i] for i in range(len(points))
                                    if points[i][1] <= max_y_1
                    ]
        points_2 = [points[i] for i in range(len(points))
                                    if min_y_2 <= points[i][1]
                    ]
    return min(closest_distance(points_1), closest_distance(points_2))


def brute_closest_distance(points):
    min_d = distance(points[0], points[1])
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            min_d = min(min_d, distance(points[i], points[j]))
    return min_d

def experiment(n, dim, max_coord):
    pts = random_points(n, dim, max_coord)
    starting = time.time()
    print(f"{n:6d} {closest_distance(pts):8.2f} {time.time() - starting:10.3}", end = " ")
    starting = time.time()
    print(f" {brute_closest_distance(pts):8.2f} {time.time() - starting:10.3}")

for n in (2**i for i in range(2, 15)):
    experiment(n, 2, 1000000)