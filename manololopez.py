#from numpy import sqrt

import math

class Point3D:

    #A point is defined by 3 coordinates
    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        def get_x(self):
        return self.x
        
        def set_x(self, x):
        self.x = x
        
        def get_y(self):
        return self.y
