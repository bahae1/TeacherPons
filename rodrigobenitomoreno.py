#from numpy import sqrt


class Point3D:

    #A point is defined by 3 coordinates
    


    #Commit 1: __init__(constructor)[DONE] , setters, getters and __str__ (tostring)
    def __init__(self):
        pass
        
    def __init__(self, cordX, cordY, cordZ):
    	self.cordX = cordX
    	self.cordY = cordY
    	self.cordZ = cordZ

    def get_cordX(self):
    	return self.cordX
    	
    def get_cordY(self):
    	return self.cordY
    	
    def get_cordZ(self):
    	return self.cordZ
    	
    def set_cordX(self):
    	self.cordX = cordX
    	
    def set_cordY(self):
    	self.cordY = cordY
    	
    def set_cordZ(self):
    	self.cordZ = cordZ
    	
    def __str__ (self)
    	return str(self.get_cordX) + " , " + str(self.get_cordY) + " , " + str(self.get_cordZ) + " ."	
    		
    #Commit 2: Distance to origin.
    def distance_to_origin(self):
    	return math.sqrt(self.get_cordX()**2+self.get_ycordY)**2+self.get_cordZ()**2)


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
