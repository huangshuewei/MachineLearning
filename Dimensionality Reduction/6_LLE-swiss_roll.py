# -*- coding: utf-8 -*-
"""
Local Linear Embedding examples
- Swiss Roll

@author: Tim Cootes
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.manifold import LocallyLinearEmbedding

# Generate spiral cone
# Number of samples
ns=2000

# Number of dimensions
nd=3

# Generate points on 2D plane, in [0,1][0,1]
R=np.random.rand(ns,2)

# Wrap the plane into a spiral
X=np.zeros([ns,nd])
X[:,0]=2*R[:,0]
X[:,1]=(0.5+R[:,1])*np.cos(2.5*np.pi*R[:,1])
X[:,2]=(0.5+R[:,1])*np.sin(2.5*np.pi*R[:,1])
     
fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.plot(X[:,0],X[:,1],X[:,2])
ax.scatter(X[:,0],X[:,1],X[:,2],c=R[:,1],cmap=plt.cm.Spectral)
plt.show()

# PCA for comparison
mean=X.mean(0)
cov=np.cov(X,rowvar=False)
eV,P=np.linalg.eigh(cov)
order=np.argsort(-eV)
P2=P[:,[order[0],order[1]]]
b=(X-mean)@P2

plt.figure(figsize=(5,5))
plt.scatter(b[:,0],b[:,1],c=R[:,1],cmap=plt.cm.Spectral)
plt.title("PCA Projection")
plt.show()


nn=15
embedding = LocallyLinearEmbedding(n_components=2, n_neighbors=nn)
y = embedding.fit_transform(X)

plt.figure(figsize=(5,5))
plt.scatter(y[:,0],y[:,1],c=R[:,1],cmap=plt.cm.Spectral)
plt.title("Local Linear Embedding of Swiss Roll, k={:d}".format(nn))
plt.show()

