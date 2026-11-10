import matplotlib.pyplot as plt
import random
import math

def random_points(n, max_coord):
    '''returns a list of n random points with integer coordinates in [0, max_coord)
as [[x0, y0], [x1, y1], [x2, y2], ... ]'''
    l = []
    for i in range(n):
        l.append([random.randint(0,max_coord), random.randint(0,max_coord)]) 
    return l

def random_values(n, max_coord):
    '''returns a list of n random integers in [0, max_coord)
as [a0, a1, a2, ... ]'''
    l = []
    for i in range(n):
        l.append(random.randint(0,max_coord)) 
    return l

if __name__ == "__main__":

    fig, ax = plt.subplots()

# using a list of points (drawn in green)
    many_points = random_points(10, 10000)
    ax.scatter([x[0] for x in many_points], [x[1] for x in many_points], color = "green")
    
# alternative, using two lists of x and y coordinates (drawn in red)

    many_x = random_values(10, 10000)
    many_y = random_values(10, 10000)
    ax.scatter(many_x, many_y, color = "red")
    
# drawing some segments
    ax.plot(many_x[0:2], many_y[0:2], color = "blue")
    ax.plot(many_x[2:7], many_y[2:7], color = "black")

# next line to show the drawing
    plt.show()


        
