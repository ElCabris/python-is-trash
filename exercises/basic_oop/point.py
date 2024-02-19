# Points problems
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x}, {self.y})'

    # calcule the distance between two points
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    # overload sub to calcule the distance between two points
    def __sub__(self, other):
        return self.distance(other)
    
    def rotation(self, radians = None, degrees = None):
        
        """This function rotates the point
        with respect to the origin"""

        if (radians == degrees == None) or (radians != None and degrees != None):
            print("error de parámetros")
        else:
            if degrees is not None:
                radians = (degrees * math.pi) / 180

            magnitude = self - Point(0,0) #magnitude of the vector (radius of the circumference)
            angule = math.acos(self.x / magnitude)
            
            #condicionales para determinar el cuadrante
            if self.y < 0:
                angule *= -1

            new_angule = angule + radians

            self.x = magnitude * math.cos(new_angule)
            self.y = magnitude * math.sin(new_angule)