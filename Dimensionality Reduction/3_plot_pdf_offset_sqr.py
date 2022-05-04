# -*- coding: utf-8 -*-
"""
Plot PDF of square of shifted PDF.
If x is from unit normal, compute pdf of y=(x+a)^2

@author: Tim Cootes
"""

import numpy as np
from scipy.stats import chi2,norm
import matplotlib.pyplot as plt


def two_sided(y,a):
    """Distribution of y=(x+a)*|x+a|"""
    ya=np.abs(y)
    b=np.sqrt(ya)
    c=np.exp(-0.5*a*a)/(np.sqrt(8*np.pi)*b)
    return c*np.exp(-0.5*(ya-2*a*b*np.sign(y)))

def one_sided(y,a):
    """Distribution of y=(x+a)**2"""
    ya=np.abs(y)
    b=np.sqrt(ya)
    c=np.exp(-0.5*a*a)/(np.sqrt(8*np.pi)*b)
    d=np.exp(-a*b)
    return c*np.exp(-0.5*ya)*(d+1/d)*(y>0)

a=4

d=np.random.normal(0,scale=1,size=5000)
d2=(d+a)**2
print("Mean: {:.2f} Var: {:.2f}".format(d2.mean(),np.var(d2)))
plt.hist(d2,bins=np.arange(-5,100,0.2))

# Avoid zero as there's a discontinuity
y=np.arange(0.5,100,0.1)
py=one_sided(y,a)

plt.plot(y,1000*py)
plt.show()

plt.figure(figsize=(6,3))
plt.ylim([0,0.08])
plt.xlim([0,100])
plt.plot(y,one_sided(y,1),color='red')
plt.plot(y,one_sided(y,3),color='green')
plt.plot(y,one_sided(y,5),color='blue')
plt.plot(y,one_sided(y,7),color='orange')
plt.axvline(0)
plt.show()
