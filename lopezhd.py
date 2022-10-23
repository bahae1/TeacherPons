#from numpy import sqrt

import math
class Point3D:

    #A point is defined by 3 coordinates
    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    
    def get_X (self):
    	return self.x
    	
    def set_X (self,x):
    	self.x = x
    
    def get_Y (self):
    	return self.y
    	
    def set_Y (self,y):
    	self.y = y
    	
    def get_Z (self):
    	return self.z
    	
    def set_Z (self,z):
    	self.z = z

        
    def __str__(self):
    	return "Valores: X: " + str(self.get_X()) + ", Y: " + str(self.get_Y()) + ", Z: " + str(self.get_Z())

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return math.sqrt(self.get_X()**2 + self.get_Y()**2 + self.get_Z()**2)


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return math.sqrt((point_2.get_X() - self.get_X())**2 + (point_2.get_Y - self.get_Y())**2 + (point2.get_Z - self.get_Z)**2)
