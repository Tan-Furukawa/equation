#%%
from sympy import *

dim = 2

C = IndexedBase("C")
k = IndexedBase("k")

i, j, m, n= symbols("i j m n")

a = Sum(C[i,j,m,n] * k[j] * k[n], (j, 1, dim), (n, 1, dim))
a = expand(a.doit())

#%%

def cubic_index_rule(index):
  if index == (1,1,1,1) or index == (2,2,2,2):
    return (1, 1)
  elif index == (1,2,1,2) or index == (2,1,1,2) or index==(2,1,2,1) or index == (1,2,2,1):
    return (4, 4)
  elif index == (1,1,2,2) or index == (2,2,1,1):
    return (1, 2)
  else:
    return None

def fix_coefficients(expression, base, index_rule, dim=2):
  for ii in range(1, dim+1):
    for jj in range(1, dim+1):
      for mm in range(1, dim+1):
        for nn in range(1, dim+1):
          index = (ii, jj, mm, nn)
          if index_rule(index) == None:
            expression = expression.subs({base[ii,jj,mm,nn]: 0})
          else:
            x = index_rule(index)
            expression = expression.subs({base[ii,jj,mm,nn]: base[x[0],x[1]]})
  return expression

def apply_matrix(mat, fn):
  m = len(mat)
  n = len(mat[0])
  newMat = [[None, None], [None, None]]
  for i in range(m):
    for j in range(n):
      newMat[i][j] = fn(mat[i][j], i, j)
  return newMat

def component (b, ii, jj):
  return fix_coefficients(a.subs({i:(ii+1), m:(jj+1)}), C, cubic_index_rule)

mat = [[0,0],[0,0]]
mat = Matrix(apply_matrix(mat, component))
#%%

mat = mat.inv()

mat

#%%

def as_matrix(expression, *symbols):
  res = []
  ri = symbols[0]
  rj = symbols[1]
  for ii in range(ri[1],ri[2]+1):
    tmp = []
    for jj in range(rj[1],rj[2]+1):
      tmp.append(expression.subs({ri[0]: ii, rj[0]: jj}))
    res.append(tmp)
  
  return res


# Matrix(as_matrix(a, (i, 1, 2), (m, 1, 2)))
# %%
