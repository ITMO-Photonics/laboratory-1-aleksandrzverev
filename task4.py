import numpy as np
import scipy.linalg as lin
import time

N=10
A = np.random.random((N,N))
k = np.arange(N)
b = np.zeros(N)
t_st = 0.
t_fin = 10.
t_del = 0.1


start_time = time.clock()
for t in np.linspace(t_st,t_fin,num = int(t_fin/t_del)):
    b = k/(1.+ k * t) 
    x_sol = lin.solve(A,b)
    print("t=",t, "x_sol=",x_sol)
print("--- %s seconds - time for solve method" % (time.clock() - start_time))

A_LU = lin.lu_factor(A)
start_time = time.clock()
for t in np.linspace(t_st,t_fin,num = int(t_fin/t_del)):
    b = k/(1.+ k * t) 
    x_LU = lin.lu_solve(A_LU, b)
    print("t=",t, "x_LU=", x_LU)
print("--- %s seconds - time for LU method" % (time.clock() - start_time))

A_inv = lin.inv(A)
start_time = time.clock()
for t in np.linspace(t_st,t_fin,num = int(t_fin/t_del)):
    b = k/(1.+ k * t) 
    x_inv = np.dot(A_inv,b) 
    print("t=",t, "x_inv=", x_inv)
print("--- %s seconds - time for inv method" % (time.clock() - start_time))
