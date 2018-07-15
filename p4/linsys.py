from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        # d_coe = MyDecimal(Decimal(coefficient))
        # if(d_coe.is_near_zero()):
        #     raise Exception('Coefficient can not be zero')

        n = self[row].normal_vector
        k = self[row].constant_term

        new_n = n.times_scalar(coefficient)
        new_k = k * coefficient

        self[row] = Plane(normal_vector=new_n, constant_term=new_k)
        return self[row]

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        n = self[row_to_add].normal_vector
        k = self[row_to_add].constant_term

        new_n = n.times_scalar(coefficient)
        new_k = k * coefficient

        row_added = self[row_to_be_added_to]

        new_n = row_added.normal_vector.plus(new_n)
        new_k = row_added.constant_term + new_k

        self[row_to_be_added_to] = Plane(
            normal_vector=new_n, constant_term=new_k)
        return self[row_to_be_added_to]

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def compute_triangular_form(self):
        system = deepcopy(self)

        print('get system')
        print(system)
        # 交换等式位置，使第一行等式第一项不为0，一共三行 = 向量的维度
        sort_row = self.dimension
        if(len(system) < sort_row):
            sort_row = len(system)

        for x in range(sort_row):
            if(system[x].normal_vector[x] != 0):
                continue
            for y in range(x+1, len(system)):
                if(system[y].normal_vector[x] != 0):
                    system.swap_rows(x, y)
                    break

        print('compute after sort')
        print(system)
        # 逐行清理首项
        # 从第n行开始(n>=2)，检查前n-1项的数字是否为0，如果不为0，用(n-1)行转换为0
        clear_dimension_index = 1
        for x in range(1, len(system)):
            if(clear_dimension_index == self.dimension):
                system[x] = Plane()
                continue
            for y in range(x):
                if(system[x].normal_vector[y] != 0):
                    row_add = y

                    r_coe = system[x].normal_vector[y] / system[row_add].normal_vector[y]
                        
                    system.add_multiple_times_row_to_row(-1 * r_coe, row_add, x)

                    # 校验 0 == 0, 出现这个等式说明可能有多解，continue, 找到下一行继续运算
                    if( sum(system[x].normal_vector) == 0 and system[x].constant_term == 0):
                        print('clear trouble: 0 = 0, continue')
                        continue

                    # 校验 0 == k, 出现这个等式说明无解，跳出循环
                    if( sum(system[x].normal_vector) == 0 and system[x].constant_term != 0):
                        print('clear trouble: 0 = k, break')
                        break

            clear_dimension_index += 1 
            # if(system[x].normal_vector[x] != 0 ):
            #     system.multiply_coefficient_and_row(1/system[x].normal_vector[x],x)

        print('compute after clear, clear {}'.format(clear_dimension_index))

        if(clear_dimension_index < self.dimension):
            print()
        print(system)
        return system

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1, p)
                for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

s = LinearSystem([p0, p1, p2, p3])

# print (s.indices_of_first_nonzero_terms_in_each_row())
# print ('{},{},{},{}'.format(s[0],s[1],s[2],s[3]))
# print (len(s))
# print (s)


# demo

# s.multiply_coefficient_and_row(2,0)
# print (s)

# s.add_multiple_times_row_to_row(3,0,2)
# print (s)

# 1
# print (s[0].normal_vector[0])

# for x in range(len(s)):
#     print(x)

# print (MyDecimal('1e-9').is_near_zero())
# print (MyDecimal('1e-11').is_near_zero())

# print ( 'swipe 1 and 2')
# s.swap_rows(0,2)
