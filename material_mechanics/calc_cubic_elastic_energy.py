#%%
# cubicの弾性エネルギーとその∇微分を計算する。
from sympy import *
from utils import *

dim = 2

C = IndexedBase("C")
C0 = IndexedBase("C^0")
Ci = IndexedBase("C^i")
t = symbols("eta")

c = symbols("c")

A = IndexedBase("A")
e = IndexedBase("epsilon")
ei = IndexedBase("epsilon^*")
i, j, l, m, n, o, p, q = symbols("i j l m n o p q")

a = Sum( C[i,j,m,n] * (e[i,j] - ei[i,j]) * (e[m,n] - ei[m,n]), 
  (i, 1, dim), (j, 1, dim), (m, 1, dim), (n, 1, dim)
)
#%%

a = expand(a.doit())

#%%

a = fix_coefficients(a, C, cubic_index_rule, 2)
#%%

a = a.subs({e[2,1]: e[1,2]})
a = a.subs({ei[2,1]: ei[1,2]})
a = a.subs({ei[1,2]: 0})
a = a.subs({ei[1,1]: t * c})
a = a.subs({ei[2,2]: t * c})

#%%

# C0 = 1/2 (Cp + Cm)
# Ci = (Cp - Cm)
# C = C0 - (1/2 - c) Ci = cCp + (1 - c)Cm
a = a.subs({C[1,1]: (C0[1,1] - (1/2-c) * Ci[1,1])})
a = a.subs({C[1,2]: (C0[1,2] - (1/2-c) * Ci[1,2])})
a = a.subs({C[4,4]: (C0[4,4] - (1/2-c) * Ci[4,4])})

a = diff(a, c)
#%%


a = a.subs({C0[1,1]: (C[1,1] + (1/2-c) * Ci[1,1])})
a = a.subs({C0[1,2]: (C[1,2] + (1/2-c) * Ci[1,2])})
a = a.subs({C0[4,4]: (C[4,4] + (1/2-c) * Ci[4,4])})


a = sympify(expand(a))

a = collect(a, c)
a
a = collect(a, Ci[1,1])
a = collect(a, Ci[1,2])

a_c = a - a.subs({c:0})
a_nc = a.subs({c:0})

a_c = factor(a_c)
# a_c = expand(a_c)
a_c

# a_c = a_c.subs({c: (C[4,4] - C0[4,4]) / Ci[4,4] + 1/2})

# a
# %%


# a = expand(a)
# a = a.doit()
# a.doit()


# b = as_matrix(a, (i, 1, dim), (m, 1, dim))

# J = b.inv()

# c = Sum(K[i, r] * k[l] * k[j] * C[r, l, m, n] * s[m, n], (l, 1, dim), (r, 1, dim), (n, 1, dim), (m, 1, dim))
# c = expand(c.doit())

# #%%
# c = c.subs({i:1, j:1})
# c = c.subs({K[1,1]: J[0,0]})
# c = c.subs({K[1,2]: J[0,1]})
# c = c.subs({K[2,1]: J[1,0]})
# c = c.subs({K[2,2]: J[1,1]})

# sympify(c.doit())




# %%
