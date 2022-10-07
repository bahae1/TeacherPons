

class Point3D:

    #A point is defined by 3 coordinates
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
