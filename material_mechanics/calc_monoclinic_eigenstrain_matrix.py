#%%

from sympy import *

def Crs(A, B): return expand(Matrix([
[A[1,0]*B[2,0]-A[2,0]*B[1,0]],
[A[2,0]*B[0,0]-A[0,0]*B[2,0]],
[A[0,0]*B[1,0]-A[1,0]*B[0,0]]
]))

def Dot(A, B): return A[0,0] * B[0,0] + A[1,0] * B[1,0] + A[2,0] * B[2,0]

def Product (A, B): return expand(Matrix([
  [A[0,0]*B[0,0], A[1,0]*B[0,0], A[2,0]*B[0,0]],
  [A[0,0]*B[1,0], A[1,0]*B[1,0], A[2,0]*B[1,0]],
  [A[0,0]*B[2,0], A[1,0]*B[2,0], A[2,0]*B[2,0]]
]).T)

def ApplyMat(A, Fn): 
  res = zeros(A.shape[0], A.shape[1]) 
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      res[i, j] = Fn(A[i,j])
  return res

var('a1:4 b1:4 c1:4')

A = Matrix([[a1],[a2],[a3]])
B = Matrix([[b1],[b2],[b3]])
C = Matrix([[c1],[c2],[c3]])

# Product(A,B)
#%%

a, b, c, beta = symbols("a, b, c \\beta")

A = A.subs({A[0]: a, A[1]: 0, A[2]: 0})
B = B.subs({B[0]: 0, B[1]: b, B[2]: 0})
C = C.subs({C[0]: c * cos(beta), C[1]: 0, C[2]: c * sin(beta)})

a_s = Crs(B, C) / (Dot(A, Crs(B, C)))
b_s = Crs(C, A) / (Dot(B, Crs(C, A)))
c_s = Crs(A, B) / (Dot(C, Crs(A, B)))

k_a, k_b, k_c = symbols("k_a, k_b, k_c")
x, x_0 = symbols("x, x_0")

K_A = Matrix([[a1],[a2],[a3]])
K_B = Matrix([[b1],[b2],[b3]])
K_C = Matrix([[c1],[c2],[c3]])

K_A = K_A.subs({
  K_A[0]: a * 0.0567,
  K_A[1]: 0,
  K_A[2]: 0
  })
K_B = K_B.subs({
  K_B[0]: 0,
  K_B[1]: b * 0.0162,
  K_B[2]: 0
  })
k_beta = -0.0116
k_c = 0.0112
K_C = K_C.subs({
  K_C[0]: -c * sin(beta) * k_beta + c * k_c * cos(beta),
  K_C[1]: 0,
  K_C[2]: c * cos(beta) * k_beta + c * k_c * sin(beta),
  })

# (Product(a_s,  K_A) + Product(b_s,  K_B) + Product(c_s,  K_C))
# epsilon = (Product(K_A,  a_s) + Product(K_B,  b_s) + Product(K_C,  c_s)) 


epsilon = \
  1/2 * (Product(K_A,  a_s) + Product(K_B,  b_s) + Product(K_C,  c_s)) \
  + 1/2 * (Product(a_s,  K_A) + Product(b_s,  K_B) + Product(c_s,  K_C))

epsilon = epsilon.subs({beta: 116 / 180 * pi})
epsilon = epsilon.evalf()
# epsilon.eigenvals()
epsilon.eigenvects()

#%%

p1 = epsilon * Matrix([1,0,0])
p3 = Dot(epsilon * Matrix([cos(beta), 0, sin(beta)]), Matrix([-sin(beta), 0, cos(beta)]))
p3 = p3.subs({beta: 116 / 180 * pi})
p3 = p3.evalf()
p3 - p1[2]

# ApplyMat(epsilon, factor)

 
#%%

