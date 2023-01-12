import numpy as np
from math import sqrt

x = 5  # this is a global variable
point = np.zeros(10)
def my_function():
    ii = 0
    while(True):
        print(point)
        #global x
        x = 10
        print(x)  # this will print 10
        point[1] = 1
        ii+=1
        if ii == 2:
            break
my_function()
print(x)   # this will also print 10
#print(point)


def distance(x1,y1,x2,y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('distance',distance(15,10,15,30))