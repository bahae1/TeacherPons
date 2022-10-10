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
