#%%
# Orville 1967の長石の格子定数のデータをRobin 1974のフォーマットに変える計算
from sympy import *
x = symbols("x")
a = 8.15328 + 0.36749 * x + 0.26874 * x**2 - 0.18688 * x**3
plot(a, (x,0,1))

aa = diff(a,x)
aa_val = aa.subs({x: 0.33})
a_val = a.subs({x: 0.33})

aa_val / a_val

#%%

b = 12.85722+0.40877 * x - 0.31560 * x**2 + 0.07217 * x**3
plot(b, (x,0,1))

bb = diff(b,x)
bb_val = bb.subs({x: 0.33})
b_val = b.subs({x: 0.33})

bb_val / b_val
#%%