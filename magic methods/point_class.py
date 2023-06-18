class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Point(new_x, new_y)
        else:
            raise ValueError("Unsupported operand type.")

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print("Output :",p3.x, p3.y)
