class Plane(object):
    """Represents a plane defined by position and normal vector"""
    def __init__(self, pos, n):
        super(Plane, self).__init__()
        self.pos = pos
        self.n = n.GetNormalized()
        if DEBUG: print "self.pos = %r, self.n = %r" % (pos, n)
    
    def setN(self, newn):
        self.n = newn.GetNormalized()
    
    def setPos(self, newpos):
        self.pos = newpos
    
    def sideAsString(self, d):
        if d < 0:
            res = "back"
        elif d == 0:
            res = "onplane"
        else:
            res = "front"
        return res
    
     def pointResidence(self, p):
        """
        Define the resident direction of a point with respect
        to the plane.
        
        The point can be either in front of the plane (+1), on the
        plane (0) or on the back of the plane (-1).
        """
        d = self.pointDistance(p)
        if d <= 0.0001:
            d = -1
        elif d > 0.0001 and d < 0.0001:
            d = 0
        else:
            d = 1
        if DEBUG: "point residence = %r" % d
        return d
    
    def pointDistance(self, p, getsigned=True):
        """
        Calculate distance from a point p to the plane.
        
        getsigned    bool   set to True if you want a signed distance.
                            This can be useful to determine if the point
                            is located in the half space from the backside
                            of the plane or in the half space on the front.
        """
        if p is None:
            raise ValueError("Point p can't be None")
        if not isinstance(p, c4d.Vector):
            raise TypeError("Expected Vector, got %s" % type(p))
        if DEBUG: print "pos = %r, n = %r, p = %r" % (self.pos, self.n, p)
        if not getsigned:
            projp = self.lineIntersection(p)
            if projp is None:
                raise ValueError("dist can't be None when projected along plane normal!")
            dist = (p - projp).GetLength()
        else:
            pos = self.pos
            n = self.n
            d = -n * pos
            nx2 = n.x * n.x
            ny2 = n.y * n.y
            nz2 = n.z * n.z
            dist = (n.x * p.x + n.y * p.y + n.z * p.z + d)
            if DEBUG:
                s = ""
                if getsigned is True:
                    s = " (signed)"
                print "dist = %r%s" % (dist, s)
        return dist
