#from numpy import sqrt


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
    	return 'X=' + str(self.x) + ',Y=' + str(self.y) + ',Z=' + str(self.z)

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return math.sqrt((pow(self.get_x())+pow(self.get_y())+pow(self.get_x))

    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return sqrt( (self.x - point_2.x)**2 + (self.y - point_2.y)**2)

    #Commit 4: Determine quadrant
    def cuadrante(self, x, y ):
        if x>0 and y>0:
            print("pertenece a Cuadrante I")
        elif x<0 and y>0:
            print("pertenece a Cuadrante II")
        elif x<0 and y<0:
            print("pertenece a Cuadrante III")
        elif x>0 and y<0:
            print("pertenece a Cuadrante IV")
        elif x== 0 and y==0:
            print("ORIGEN")


    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass


if __name__ == "__main__":
    pass
