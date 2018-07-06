from math import sqrt, acos
import math as math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Can not normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        result = [Decimal(obj) * x for x in self.coordinates]
        return Vector(result)

    def magnitude(self):
        pow_2_list = [Decimal(x)**2 for x in self.coordinates]
        return  Decimal(str(sqrt(sum(pow_2_list))))

    def normalize(self):
        try:
            self_mag = self.magnitude()
            return self.times_scalar(Decimal('1.0')/self_mag)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, obj):
        result = [x*y for x, y in zip(self.coordinates, obj.coordinates)]
        return sum(result)

    def angle(self, obj, in_degree=False):
        try:
            u1 = self.normalize()
            u2 = obj.normalize()
            
            res = math.acos(u1.dot(u2))
            if in_degree:
                res = res * 180. / math.pi
            return res
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e

    def is_zero_vector(self):
        return sum([x for x in self.coordinates]) == 0

    def is_parallel(self, obj, tolerance=1e-10):
        if self.is_zero_vector() or obj.is_zero_vector():
            return True

        u1 = self.normalize()    
        u2 = obj.normalize()
        abs_dot = round(abs(u1.dot(u2)),10)

        print('dot is {}'.format(abs_dot))
        return (abs_dot > (1 - tolerance)) and (abs_dot < (1 + tolerance))

    def is_orthogonal(self, obj, tolerance=1e-10):
        if self.is_zero_vector() or obj.is_zero_vector():
            return True
        u1 = self.normalize()    
        u2 = obj.normalize()
        dot = round(abs(u1.dot(u2)),10)
        print('dot is {}'.format(dot))
        return abs(dot) <= tolerance
    
    # 获取向量在base向量上的投影
    def component_parallel_to(self,base):
        try:
            u_b = base.normalize()
            m_v = self.dot(u_b)
            return u_b.times_scalar(m_v)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e

    # 获取向量在base向量上的投影向量的另一直角边向量
    def component_orthogonal_to(self,base):
        try:
            pro_self = self.component_parallel_to(base)
            return self.minus(pro_self)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e

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


# s1 = Vector(['7.887', '4.138'])
# s2 = Vector(['-8.802', '6.776'])
# print(s1.dot(s2))

# s1 = Vector(['-5.955', '-4.904', '-1.874'])
# s2 = Vector(['-4.496', '-8.755', '7.103'])
# print(s1.dot(s2))

# s1 = Vector(['3.183', '-7.627'])
# s2 = Vector(['-2.668', '5.319'])
# print(s1.angle(s2))

# s1 = Vector(['7.35', '0.221', '5.188'])
# s2 = Vector(['2.751', '8.259', '3.985'])
# print(s1.angle(s2, True))

# s1 = Vector(['-7.579', '-7.88'])
# s2 = Vector(['22.737', '23.64'])

# s1 = Vector(['-2.029', '9.97', '4.172'])
# s2 = Vector(['-9.231', '-6.639', '-7.245'])

# s1 = Vector(['2.118', '4.827'])
# s2 = Vector(['0', '0'])

# s1 = Vector(['-2.328', '-7.284', '-1.214'])
# s2 = Vector(['-1.821', '1.072', '-2.94'])

# print(s1.is_parallel(s2))
# print(s1.is_orthogonal(s2))

# v = Vector(['3.039','1.879'])
# w = Vector(['0.825','2.036'])
# pro_v =  v.projection(w)
# print(pro_v)

# v = Vector(['-9.88','-3.264','-8.159'])
# w = Vector(['-2.155','-9.353','-9.473'])
# print (v.projection_orthogonal(w))

v = Vector(['3.009','-6.172','3.692','-2.51'])
w = Vector(['6.404','-9.144','2.759','8.718'])
pro = v.component_parallel_to(w)
pro_orh = v.component_orthogonal_to(w)
sum_p_po = pro.plus(pro_orh)

print (pro)
print (pro_orh)
print (sum_p_po)

# v = Vector([3.039,1.879])
# print(v)
# w = Vector(['3.039','1.879'])
# print(w)