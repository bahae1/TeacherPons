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
    
     #Commit 4: Determine quadrant
    def calculate_quadrant(self):
     	#Devuelve 0 si está en el origen de coordenadas o sobre alguno de los ejes.
        if (self.get_X() == 0 or self.get_Y == 0):
            return 0;
        #Devuelve 1 si está en el primer cuadrante (x e y positivos).
        if (self.get_X() > 0 and self.get_Y > 0):
            return 1;
        #Devuelve 2 si está en el segundo cuadrante (x negativo e y positivo).
        if (self.get_X() < 0 and self.get_Y > 0):
            return 2;
        #Devuelve 3 si está en el tercer cuadrante (x e y negativos).
        if (self.get_X() < 0 and self.get_Y < 0):
            return 3;
        #Devuelve 4 si está en el cuarto cuadrante (x positivo e y negativo).
       	if (self.get_X() > 0 and self.get_Y < 0):
            return 4;
    
        #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        minimo = sys.maxsize
        cercano = None
        
        for point in points:
            distancia = self.calculate_distance(point)
            
            if distancia < minimo:
                cercano = point
                minimo = distance
        return cercano

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
if __name__ == "__main__":
    pass
