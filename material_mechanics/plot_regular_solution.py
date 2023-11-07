#%%
# 正則溶液のプロットをする
from sympy import *

mu = IndexedBase("mu")
X = IndexedBase("X")

i = symbols("i")
R = symbols("R")
T = symbols("T")
w = symbols("w")
c = symbols("c")
N = symbols("N")

g0 = R * T * (c * log (c) + (1-c) * log(1-c)) + w * R * T * c * (1-c)
g1 = R * T * (c * log (c) + (1-c) * log(1-c)) - w * R * T * c ** 2
g2 = R * T * (c ** 2 * (1-c)**2)
#%%

r = (c, 0.01, 0.99)
g0 = g0.subs({w:3, R:8.31, T:300})
plot(g0, r)
plot(diff(g0,c), r)

g1 = g1.subs({w:5, R:8.31, T:300})
plot(g1, r)
plot(diff(g1,c), r)
#%%



