# import numpy as np

# def plus(s1,s2):
#     return s1+s2

# def minus(s1,s2):
#     return s1-s2

# def scal(s1,s2):
#     res = s1*s2
#     return [ round(i,3) for i in res]
#     # return round(s1 * s2,3)

# s1 = np.array([8.218,-9.341])
# s2 = np.array([-1.129,2.111])
# print(plus(s1,s2))

# s3 = np.array([7.119,8.215])
# s4 = np.array([-8.223,0.878])
# print(minus(s3,s4))

# s5 = 7.41
# s6 = np.array([1.671,-1.012,-0.318])
# print(scal(s5,s6))

a1 = [1,2,3]
a2 = 0
for x in a1:
    a2+=x
print(a2)