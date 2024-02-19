class Shape(object):
    
    width: float
    height: float


class Rectangle(Shape):
    """Définit un rectangle."""

    
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectange(width={self.width}, height={self.height})"

    def set_width(self, width: float) -> None:
        self.width = width
        
    def set_height(self, height: float) -> None:
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Trop grand pour en faire une image."
        else:
            return ("*" * int(self.width) + "\n") * int(self.height)

    def get_amount_inside(self, shape: Shape):
        return int(self.width / shape.width) * int(self.height / shape.height)


class Square(Rectangle):
    
    def __init__(self, width_and_height: float) -> None:
        super().__init__(width_and_height, width_and_height)

    def __str__(self) -> str:
        return f"Carre(side={self.width})"

    @property
    def side(self) -> float:
        return self.width
    
    @side.setter
    def side(self, side: float) -> None:
        self.set_side(side)

    def set_side(self, side: float) -> None:
        self.height = side
        self.width = side

    def set_width(self, width: float) -> None:
        self.set_side(width)

    def set_height(self, height: float) -> None:
        self.set_side(height)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.height=3
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
sq = Square(9)
print(sq.get_area())
sq.side=4
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.height=8
rect.width=16
print(rect.get_amount_inside(sq))
