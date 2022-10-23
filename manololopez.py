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
    
    def set_y(self, y):
        self.y = y
        
    def get_z(self):
        return self.z
        
    def set_z(self, z):
        self.z = z
        
    def __str__(self):
        return "X: " + str(self.x) + ",Y: " + str(self.y) + ",Z: " + str(self.z)
        

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
