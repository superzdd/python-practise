from math import sqrt,acos
import math as math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, obj):
        result = [x + y for x, y in zip(self.coordinates, obj.coordinates)]
        return Vector(result)

    def minus(self, obj):
        result = [x - y for x, y in zip(self.coordinates, obj.coordinates)]
        return Vector(result)

    def times_scalar(self, obj):
        result = [x * obj for x in self.coordinates]
        return Vector(result)

    def magnitude(self):
        pow_2_list = [x**2 for x in self.coordinates]
        return sqrt(sum(pow_2_list))

    def normalize(self):
        try:
            self_mag = self.magnitude()
            return self.times_scalar(1.0/self_mag)
        except ZeroDivisionError:
            raise Exception('Can not normalize the zero vector')

    def dot(self, obj):
        result = [x*y for x, y in zip(self.coordinates, obj.coordinates)]
        return sum(result)

    def angle(self, obj):
        cos_res = self.dot(obj)/(self.magnitude() * obj.magnitude())
        return math.acos(cos_res)

    def degree(self, obj):
        degree_res = self.angle(obj)
        return degree_res * 180 / math.pi

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

# s1 = Vector([8.218,-9.341])
# s2 = Vector([-1.129,2.111])
# print(s1.plus(s2))

# s3 = Vector([7.119,8.215])
# s4 = Vector([-8.223,0.878])
# print(s3.minus(s4))

# s5 = 7.41
# s6 = Vector([1.671,-1.012,-0.318])
# print(s6.times_scalar(s5))

# s1 = Vector([-0.221,7.437])
# print( s1.magnitude() )

# s2 = Vector([8.813,-1.331,-6.247])
# print( s2.magnitude() )

# s3 = Vector([5.581,-2.136])
# print( s3.normalize() )

# s4 = Vector([1.996,3.108,-4.554])
# print( s4.normalize() )


s1 = Vector([7.887, 4.138])
s2 = Vector([-8.802, 6.776])
print(s1.dot(s2))

s1 = Vector([-5.955, -4.904, -1.874])
s2 = Vector([-4.496, -8.755, 7.103])
print(s1.dot(s2))

s1 = Vector([3.183, -7.627])
s2 = Vector([-2.668, 5.319])
print(s1.angle(s2))

s1 = Vector([7.35, 0.221, 5.188])
s2 = Vector([2.751, 8.259, 3.985])
print(s1.degree(s2))
