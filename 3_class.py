class Point:
    # class attribute, same across all instances
    default_color: str = "red"

    # constructor | magic method | instance method
    def __init__(self, x: int, y: int) -> None:
        # private attribute
        self.__point_weight: int = x + y
        # instance attribute
        self.x = x
        self.y = y

    # getter property / read
    @property
    def point_weight(self):
        return self.__point_weight

    # setter property / write
    @point_weight.setter
    def point_weight(self, value: int):
        if self.x + self.y != value:
            raise ValueError("Invalid point weight")
        self.__point_weight = value

    # reimplementing magic method | https://rszalski.github.io/magicmethods/
    def __str__(self) -> str:
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y

    def __gt__(self, __value: object) -> bool:
        return self.x > __value.x and self.y > __value.y

    def __add__(self, __value: object):
        return Point(self.x + __value.x, self.y + __value.y)

    @classmethod
    def init(cls):
        return cls(x=0, y=0)

    # instance method
    def draw(self):
        print(f"Point - x:{self.x} y:{self.y}")


point_1: Point = Point(2, 2)
point_1.draw()
point_1.point_weight = 4

point_2: Point = Point.init()
point_2.x = 1
point_2.y = 1
point_2.draw()

print(point_1)
print(str(point_2))
print(point_1 == point_2)
print(point_1 > point_2)
print(point_1 + point_2)
