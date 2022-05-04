# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 08:47:44 2022

Plot n choose k
@author: Tim Cootes
"""

import numpy as np
import matplotlib.pyplot as plt


n=100
y=np.ones(n)
x=np.arange(1,n+1)

t=1.0
for i in range(1,n):
    t=t*(n-i)/i
    y[i]=t
    
plt.figure(figsize=(6,3))
plt.semilogy(x,y)
plt.show()

x=np.arange(-1,1,0.02)
y=x*np.abs(x)
plt.figure(figsize=(4,4))
plt.axvline(0,color='black')
plt.axhline(0,color='black')
plt.plot(x,y)

