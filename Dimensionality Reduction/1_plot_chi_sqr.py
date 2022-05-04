# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Plotting chi-squared distributions
@author: Tim Cootes
"""

import numpy as np
from scipy.stats import chi2,norm
import matplotlib.pyplot as plt

def gauss_approx(x,n):
    var=2*n
    y=np.exp(-(x-n)**2/(2*var))
    return y/np.sqrt(2*np.pi*var)

n1=10
n2=50
n3=100

x1=np.arange(0,150,0.5)
y1=chi2.pdf(x1,n1)
y1_gauss=gauss_approx(x1,n1)

y2=chi2.pdf(x1,n2)
y2_gauss=gauss_approx(x1,n2)

y3=chi2.pdf(x1,n3)
y3_gauss=gauss_approx(x1,n3)

plt.plot(x1,y1,color='red')
plt.plot(x1,y1_gauss,color='green')
plt.plot(x1,y2,color='red')
plt.plot(x1,y2_gauss,color='green')
plt.plot(x1,y3,color='red')
plt.plot(x1,y3_gauss,color='green')
plt.show()

