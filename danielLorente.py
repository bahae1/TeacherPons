#from numpy import sqrt


class Point3D:

    #A point is defined by 3 coordinates
    def __init__(self, x, y, z):
        self.x = x;
        self.y = y;
        self.z = z;
        
    def get_x(self):
    	return self.x
    def get_y(self):
    	return self.y
    def get_z(self):
    	return self.z
    
    def set_x(self, x):
    	self.x = x
    def set_y(self, y):
	self.y = y
    def set_z(self, z):
	self.z = z
    
    def __str__(self):
    	return "Punto 3D (x = " + str(self.get_x()) + " y = " + str(self.get_y()) + " z = " + 			str(self.get_y())
     

    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def __init__(self):
        pass

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return sqrt((self.x - 0)**2 + (self.y - 0)**2 + (self.z - 0)**2)


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return sqrt((self.x - point_2.get_x())**2 + (self.y - point_2.get_y())**2 + (self.z - point_2.get_z())**2)

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
        distanciaMinima = 9999
        distanciaFinal = 0
        
        for punto in points:
        	distancia = calculate_distance(self, punto)
        	if(distancia < distanciaMinima)
        		distanciaFinal = distancia
        		distanciaMinima = distancia


if __name__ == "__main__":
    pass
    
    
    
    
    
    
    
    
    
    
    
    
