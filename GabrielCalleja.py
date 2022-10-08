#from numpy import sqrt


class Point3D:


    #A point is defined by 3 coordinates
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __init__(self):
        pass


    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x


    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y


    def getZ(self):
        return self.z

    def setZ(self, z):
        self.z = z



    def __str__(self):
        return self.x + ", " + self.y + ", " + self.z







    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return
        math.sqrt((self.x)^2 + (self.y)^2
         + (self.z)^2)


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return math.sqrt(math.abs(self.getX - point_2.getX)^2 + math.abs(self.getY - point_2.getY)^2 + math.abs(self.getZ - point_2.getZ)^2)

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):

        if(self.x == 0 || self.y == 0 || self.z == 0):
            return 0
        elif(self.x>0):
            if(self.y>0):
                #si x e y son positivos
                return 1
            else:
                #si x es positivo e y es negativo
                return 4
        elif(self.y>0):
            #x negativo e y positivo
            return 2
        else:
            #x negativo e y negativo
            return 3

        #Devuelve 0 si está en el origen de coordenadas o sobre alguno de los ejes.
        #Devuelve 1 si está en el primer cuadrante (x e y positivos).
        #Devuelve 2 si está en el segundo cuadrante (x negativo e y positivo).
        #Devuelve 3 si está en el tercer cuadrante (x e y negativos).
        #Devuelve 4 si está en el cuarto cuadrante (x positivo e y negativo).



    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass


if __name__ == "__main__":
    pass
