# -*- coding: utf-8 -*-
"""
Local Linear Embedding example: Spiral cone

@author: Tim Cootes
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.manifold import LocallyLinearEmbedding

# Generate spiral cone
# Number of samples
ns=100

# Number of dimensions
nd=3

X=np.zeros([ns,nd])
for i in range(0,ns):
    X[i,0]=i
    X[i,1]=np.sqrt(i)*np.cos(i/5)
    X[i,2]=np.sqrt(i)*np.sin(i/5)
    
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X[:,0],X[:,1],X[:,2])
ax.scatter(X[:,0],X[:,1],X[:,2])
plt.show()

embedding = LocallyLinearEmbedding(n_components=2, n_neighbors=3)
y = embedding.fit_transform(X)

plt.figure(figsize=(5,5))
plt.plot(y[:,0],y[:,1],'go')
plt.title("Local Linear Embedding of Spiral, k=3")
plt.show()

# Repeat, adding some noise
Xn=X+np.random.normal(size=X.shape, scale=0.5)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X[:,0],X[:,1],X[:,2])
ax.scatter(Xn[:,0],Xn[:,1],Xn[:,2],color='red')
plt.show()

yn = embedding.fit_transform(Xn)

plt.figure(figsize=(5,5))
plt.plot(yn[:,0],yn[:,1],'go')
plt.title("LLE of Noisy Spiral, k=3")
plt.show()
