import math
#Espero qu funcione este commit porque sino la camiseta se la va a llevar Piter
class Point3D:

    #A point is defined by 3 coordinates(x, y , z)
    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def __init__(self, punt_x, punt_y, punt_z):
        self.punt_x = punt_x
        self.punt_y = punt_y
        self.punt_z = punt_z

    def __init__(self):
        pass

     def get_x(self):
        return self.punt_x

    def set_x(self, punt_x):
        self.punt_x = punt_x

    def get_y(self):
        return self.punt_y

    def set_y(self, punt_y):
        self.punt_y = punt_y

    def get_z(self):
        return self.punt_z

    def set_z(self, punt_z):
        self.punt_z = punt_z

    def __str__(self):
        return str(self.get_x) + ", " + str(self.get_y) + ", " + str(self.get_z) + "."

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

