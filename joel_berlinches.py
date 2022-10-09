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
    	
    def __str__(self, x, y, z):
    	return "X: " + str(self.get_x()) + ", Y: " + str(self.get_y()) + ", Z: " + str(self.get_z())
    	

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return math.sqrt(self.get_x()**2+self.get_y()**2+self.get_z()**2)


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return math.sqrt((point_2.get_x()-self.get_x())**2+(point_2.get_y()-self.get_y())**2)

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
        #Devuelve 0 si está en el origen de coordenadas o sobre alguno de los ejes.
        if (self.get_x == 0 and self.get_y == 0) or (self.get_x == 0) or (self.get_y == 0):
        	return 0
        #Devuelve 1 si está en el primer cuadrante (x e y positivos).
        if self.get_x > 0 and self.get_y > 0:
        	return 1
        #Devuelve 2 si está en el segundo cuadrante (x negativo e y positivo).
        if self.get_x < 0 and self.get_y > 0:
        	return 2
        #Devuelve 3 si está en el tercer cuadrante (x e y negativos).
        if self.get_x < 0 and self.get_y < 0:
        	return 1
        #Devuelve 4 si está en el cuarto cuadrante (x positivo e y negativo).
        if self.get_x > 0 and self.get_y < 0:
        	return 1


    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass


if __name__ == "__main__":
    pass
