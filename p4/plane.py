from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def is_parallel_to(self,other):
        # 取两条直线的法向量，观察是否平行
        # 如果平行，在other上取2点与self做法向量，观察是否与两条直线的法向量都垂直
        vert_self = self.normal_vector
        vert_other = other.normal_vector

        return vert_self.is_parallel(vert_other)
    
    def is_equal_to(self,other):
        # b_self = self.basepoint
        # b_other = other.basepoint
        # l = b_self.minus(b_other)
        # return l.is_orthogonal(self.normal_vector) and l.is_orthogonal(other.normal_vector)
        a_1,b_1,c_1 = self.normal_vector
        a_2,b_2,c_2 = other.normal_vector
        k_1 = self.constant_term
        k_2 = other.constant_term

        p_1 = a_1/a_2
        cv_b_1 = p_1*b_2
        cv_c_1 = p_1*c_2 
        cv_k_1 = p_1*k_2

        eq_b = MyDecimal(cv_b_1 - b_1).is_near_zero()
        eq_c = MyDecimal(cv_c_1 - c_1).is_near_zero()
        eq_k = MyDecimal(cv_k_1 - k_1).is_near_zero()

        return eq_b and eq_c and eq_k

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def __eq__(self, v):
        return self.normal_vector == v.normal_vector and self.constant_term == v.constant_term

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

p_1 = Plane(Vector(['-0.412','3.806','0.728']),-3.46)
p_2 = Plane(Vector(['1.03','-9.515','-1.82']),8.65)

# p_1 = Plane(Vector(['2.611','5.528','0.283']),4.6)
# p_2 = Plane(Vector(['7.715','8.306','5.342']),3.76)

# p_1 = Plane(Vector(['-7.926','8.625','-7.212']),-7.952)
# p_2 = Plane(Vector(['-2.642','2.875','-2.404']),-2.443)


is_p = p_1.is_parallel_to(p_2)
is_e = p_1.is_equal_to(p_2)

# print ('Is parallel: {}'.format( str( is_p ) ))
# print ('Is equal: {}'.format( str( is_e ) ))
