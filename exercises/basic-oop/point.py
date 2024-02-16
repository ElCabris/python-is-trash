# Points problems

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

def main():
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    # print formated string
    print(f'p1: {p1}')
    print(f'p2: {p2}')
    print(f'distance: {p1.distance(p2)}')
    print(f'distance with point sub: {p1 - p2}')


if __name__ == '__main__':
    main()
