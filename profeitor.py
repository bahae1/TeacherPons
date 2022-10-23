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
	
    fet __str__(self):
	return 'Punto 3D (x=' + str(self.get_X()) +', y=' + str(self.get_y()) +', z=' + str(self.get_z()) +')'

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return math.sqrt(self.get_x()**2+self.get_y()**2+self.get_z()**2)

    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return math.sqrt((point_2.get_x()-self.get_x())**2+(point_2.get_y()-self.get_y())**2)

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
        if self.get_x() == 0 or self.get_y() == 0 or self.get_z() == 0:
            return 0
        if self.get_x() > 0 and self.get_y() > 0:
            return 1
        if self.get_x() < 0 and self.get_y() > 0:
            return 2
        if self.get_x() < 0 and self.get_y() < 0:
            return 3
        if self.get_x() > 0 and self.get_y() < 0:
            return 4

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        pass


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        pass
