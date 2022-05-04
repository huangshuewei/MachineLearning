# -*- coding: utf-8 -*-
"""
Demonstrating Chi-Squared distribution
"""

import numpy as np
from scipy.stats import chi2,norm
import matplotlib.pyplot as plt

n_samples=1000
nd=15

d=np.random.normal(0,scale=1,size=[n_samples,nd])
c=np.sum(d*d,axis=1) # Sum along the rows after squaring

bin_width=0.5
x=np.arange(0,30,bin_width)
plt.hist(c,bins=x)
plt.plot(x,chi2.pdf(x,nd)*n_samples*bin_width)
plt.show()

