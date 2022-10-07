#from numpy import sqrt


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
    	return  "X: " + str(self.get_X()) + ", Y: " + str(self.get_Y()) + ", Z: " + str(self.get_Z())

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        pass


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        pass

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
        #Devuelve 0 si está en el origen de coordenadas o sobre alguno de los ejes.
        #Devuelve 1 si está en el primer cuadrante (x e y positivos).
        #Devuelve 2 si está en el segundo cuadrante (x negativo e y positivo).
        #Devuelve 3 si está en el tercer cuadrante (x e y negativos).
        #Devuelve 4 si está en el cuarto cuadrante (x positivo e y negativo).
        pass


    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass


if __name__ == "__main__":
    pass
