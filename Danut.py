#from numpy import sqrt


class Point3D:

    

    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def_init_(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        int valor= Math.sqrt(((self.get_x)**2+(self.get_y)**2+(self.get_z))**2);
        return valor
        

    def get_x(self):
        return self.x
    
    def set_x(self,x):
        self.x=x

    def get_y(self):
        return self.y
    
    def set_y(self,y):
        self.y=y

    def get_z(self):    
        return self.z
    
    def set_z(self,z):
        self.z=z

    def__str__(self):
        return str(self.get_x())+", "+str(self.get_y())+", "+str(self.get_z())+", "
    
    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
       int valor= Math.sqrt((self.get_x-self.get_y)**2+(point_2.get_x-point_2.get_y)**2);
        return valor



    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass


if __name__ == "__main__":
    pass
