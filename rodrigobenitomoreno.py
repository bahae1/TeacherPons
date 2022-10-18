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
    	return math.sqrt(self.get_cordX()**2+self.get_cordY)**2+self.get_cordZ()**2)


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
    	return math.sqrt((point_2.get_cordX()-self.cordX())**2+(point_2.cordY()-self.cordY())**2)

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
    	if self.get_cordX() == 0 or self.get_cordY() == 0 or self.get_cordZ() == 0:
            return 0
        if self.get_cordX() > 0 and self.get_cordY() > 0:
            return 1
        if self.get_cordX() < 0 and self.get_cordY() > 0:
            return 2
        if self.get_cordX() < 0 and self.get_cordY() < 0:
            return 3
        if self.get_cordX() > 0 and self.get_cordY() < 0:
            return 4


    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        closest_distance = sys.maxsize
        possible_point = None
        for point in points:
            distance = self.calculate_distance(point)
            if distance < closest_distance:
                possible_point = point
                closest_distance = distance
        return possible_point


if __name__ == "__main__":
    pass
