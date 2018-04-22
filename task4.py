import numpy as np
import scipy.linalg as lin
N = 100
k = 1
t_st = 0.
t_fin = 10.
del_t = 0.1
A=np.random.random((N,N))
i,j = np.indices(A.shape)
t = np.linspace(t_st, t_fin, num = int(t_fin/del_t))
B = k/(1+k*t)
x_sol = lin.solve(A,B)
A_LU = lin.lu_factor(A)
x_LU = lin.lu_solve(A_LU,B,0)
A_inv = lin.inv(A)
x_inv = np.dot(A_inv,B)
print ("x_sol = ",lin.solve(A,B))
print ("x_LU = ",lin.lu_solve(A_LU,B,0))
print ("x_inv = ",np.dot(A_inv,B))
print('solve_time = ')
(get_ipython().run_line_magic('timeit', 'lin.solve(A,B)'))
print("lu_solve_time")
get_ipython().run_line_magic('timeit', 'lin.lu_solve(A_LU,B,0)')
print("dot_solve_time")
get_ipython().run_line_magic('timeit', 'np.dot(A_inv,B)')
