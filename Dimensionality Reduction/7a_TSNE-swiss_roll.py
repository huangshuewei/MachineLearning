# -*- coding: utf-8 -*-
"""
t-SNE examples - Swiss roll

@author: Tim Cootes
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.manifold import TSNE

# Generate Swiss roll
# Number of samples
ns=1000

# Number of dimensions
nd=3

# Generate points on 2D plane, in [0,1][0,1]
R=np.random.rand(ns,2)

# Wrap the plane into a spiral
X=np.zeros([ns,nd])
X[:,0]=2*R[:,0]
X[:,1]=(0.5+R[:,1])*np.cos(3*np.pi*R[:,1])
X[:,2]=(0.5+R[:,1])*np.sin(3*np.pi*R[:,1])
    
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(X[:,0],X[:,1],X[:,2],c=R[:,1],cmap=plt.cm.Spectral)
plt.show()

embedding = TSNE(n_components=2,perplexity=100)
y = embedding.fit_transform(X)

plt.figure(figsize=(5,5))
plt.scatter(y[:,0],y[:,1],c=R[:,1],cmap=plt.cm.Spectral)
plt.title("t-SNE Embedding of Swiss Roll")
plt.show()

