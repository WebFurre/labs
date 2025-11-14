import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
    def get_square(self):
        return (self.radius**2)*math.pi
    def get_diametr(self):
        return self.radius*2

krug1 = Circle(3)
print("Текущий радиус:", krug1.get_radius())
krug1.set_radius(9)
print("Новый радиус:", krug1.get_radius())
print("Текущая площадь:", krug1.get_square())
print("Текущая диаметр:", krug1.get_diametr())