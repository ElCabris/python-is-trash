class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, otroPunto):
        lasx = otroPunto.x - self.x
        lasy = otroPunto.y - self.y
        
        return ((lasx ** 2) + (lasy ** 2)) ** (1/2)

punto_1 = Punto(4, 5)
punto_2 = Punto(9, -3)

print(punto_2 - punto_1)
