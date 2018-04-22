import numpy as np
import scipy.linalg as lin
n = 100
A = np.zeros((n,n))
i,j=np.indices(A.shape)
A[i==j]=1
A[i==j+1]=1
A[i==j+2]=1
B = np.arange((n))
Matrix = lin.solve(A,B)
Matrix
