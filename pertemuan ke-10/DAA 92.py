import numpy as np
from scipy.optimize import linprog
A=np.array([[1,1],[3,4],[-1,0],[0,-1]])
b=np.array([16,55,0,0])
C=np.array([-1,-1])
res=linprog(C,A_ub=A,b_ub=b)
print('Optimal value:', round(res.fun*-1, ndigits=2),
      '\nx values: ', res.x,
      '\nNumbuer of iterations performed: ', res.nit,
      '\nStatus: ', res.message)

