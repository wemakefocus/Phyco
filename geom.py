import alg
from math import sqrt
import error

class geom():
    pass

class line(geom):

    def __init__(self, *args, mode = '2p'):
        """generic line generator

        Different types of arguments can be used
        to define a line. Accepted forms of
        arguments are slope-intercept, point-slope
        two-point, intercept form and general form.
        All types of definition use two arguments.
        Since the constructor accept just positional
        args, please carefully follow the sequence
        of args.
        slope-intercept: m, b
        point-slope: point, slope
        two-point: not required
        intercept: x-intercept then y
        general form:coeffs of x, y, const in sequence.
        mode code are listed below:
        slope-intercept(si), point-slope(ps)
        two-point(2p),intercept(ii),general(ge)
        NOTE: POINT SHOULD BE GIVEN IN VECTOR FORM!

        """
        # only limited forms are implemented
        if mode == '2p':
            p1, p2 = args
            self.dir = p2 - p1
            self.dir = self.dir.unitize()  # unitize direction vector
            self.p = p1  # choose a point on a line
        elif mode == 'ps':
            self.p, self.dir = args
            self.dir = self.dir.unitize()
        elif mode == 0:  # used to generate class-type
            pass
        else:
            raise error.UnderConstruction

    def distance(self, arg):
        """calculate the distance between the line and an object

        It also calculates distance between skew segments as lines!

        """
        if isinstance(arg, vectortype):  # distance between point and line
            # the projection the link between the point and a point on the line.
            d = (self.p - arg) * self.dir
            # distance between the two points
            D = abs(self.p - arg)
            return sqrt(D * D - d * d)
        elif isinstance(arg, linetype):  # distance between (skew) lines
            N = self.dir.cross(arg.dir).unitize()  # common normal vector
            return N.dot(self.p - arg.p)
        raise TypeError

    def isOnLine(self, point):
        v1 = self.p - point
        v2 = self.p + self.dir - point
        if v1.isCollinear(v2):
            return True
        return False

    def __getitem__(self, x):
        raise error.UnderConstrution
        return alg.vector()

class segment(line):

    def __init__(self, p1, p2):
    # different with line, only accept two-point def
        line.__init__(self, p1, p2)
        self.endpoint1 = p1
        self.endpoint2 = p2
        self.range = [p1.x, p2.x]
        self.range.sort()
        self.vector = p2 - p1
        self.isPoint = False
        if p1 == p2:
            self.isPoint = True

    def isIntersect(self, other):
        if self.vector.cross(other.endpoint1 - self.endpoint1)\
                        .dot(other.endpoint2 - self.endpoint1) <= 0:
            if self.isPoint:
                if other.isOnSeg(self):
                    return True
                return False
            elif other.isPoint:
                if self.isOnSeg(other):
                    return True
                return False
            elif not (self.isPoint and other.isPoint):
                return True
        return False

    def isOnSeg(self, point):
        if not self.isPoint:
            if self.isOnLine(point) and\
               self.range[1] > point.x > self.range[0]:
                return True
            return False

    def __str__(self):
        return str([str(self.endpoint1), str(self.endpoint2)])

class polygon(geom):

    def __init__(self, *args):
        self.vertex = args
        self.n = len(self.vertex)

    def __sort(self):
        C = alg.vector(sum(A[0] / self.n for A in self.vertex),
                   sum(A[1] / self.n for A in self.vertex))
        det = []
        for i in self.vertex:
            t = i - C
            det = [t.cross(i) for i in self.vertex]
        for i in det:
            pass

    def __matrize(self):
        pass

    def __chebCenter(self):
        pass

class circle(geom):

    def __init__(self, center = alg.vector(), radius = None):
        self.center = center
        self.radius = radius

class funcCurve(geom):

    def __init__(self, x = None, y = None):
        pass

linetype = type(line(mode = 0))
vectortype = type(alg.vector())
circletype = type(circle())
