#from numpy import sqrt


class Point3D:

    #A point is defined by 3 coordinates
    def __init__(self, x, y, z):
	self.x = x
	self.y = y
	self.z = z
    


    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def get_x(self):
	return self.x 

    def get_y(self):
	return self.y

    def get_z(self):
	return self.z

    def get_x(self, x):
	self.x = x

    def get_y(self, y):
	self.y = y

    def get_z(self, z):
	self.z = z
