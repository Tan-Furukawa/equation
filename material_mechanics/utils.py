from sympy import *

def as_matrix(expression, *symbols):
  res = []
  ri = symbols[0]
  rj = symbols[1]
  for ii in range(ri[1],ri[2]+1):
    tmp = []
    for jj in range(rj[1],rj[2]+1):
      tmp.append(expression.subs({ri[0]: ii, rj[0]: jj}))
    res.append(tmp)
  
  return Matrix(res)

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

def ApplyMat(A, Fn): 
  res = zeros(A.shape[0], A.shape[1]) 
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      res[i, j] = Fn(A[i,j])
  return res
