

class Shape:
    def __init__(self):
        pass

    def square (self, s):
        return s * s

    def rectangle (self, l, w):
        return l * w

    def triangle (self, b, h):
        return 0.5 * b * h

    def circle (self, r):
        return 3.142 * r ** 2

    def parallelogram ( self , b , h):
        return b * h

    def trapezoid (self, p_s1, p_s2, h):
        return 0.5 * (p_s1 + p_s2) * h

    def rhombus ( self, b, h ):
        return b * h

    def ellipse (self, s_ma_a, s_m_a):
        return 3.142 * s_ma_a * s_m_a

    def regular_polygon(self, p, a):
        return (p * a) / 2

    def sector_of_circle(self, r, a):
        return (a / 360) * 3.142 * r ** 2

    def ring(self, outer_radius, inner_radius):
        return 3.142 * (outer_radius ** 2 - inner_radius ** 2)

    # def quadrilateral(self, d1):
    #     return 0.5 * d1 *


shape = Shape()
print("Square Area: ", shape.square(5))
print("Rectangle Area: " , shape.rectangle(4, 7))
print("Triangle Area: ", shape.triangle(3, 8))
print("Circle Area: " , shape.circle(5))
print("Parallelogram Area: ", shape.parallelogram(4, 7))
print("Trapezoid Area: ", shape.trapezoid(3, 6, 4))
print("Rhombus Area: ", shape.rhombus(5, 7))
print("Ellipse Area:" , shape.ellipse(3, 9))
print("Regular Polygon Area: ", shape.regular_polygon(2, 5))
print("Sector of Circle Area: ", shape.sector_of_circle(6, 9))
print("Ring Area: ", shape.ring(8, 6))
