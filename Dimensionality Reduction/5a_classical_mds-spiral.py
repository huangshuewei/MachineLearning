# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:55:22 2022

Example of classical Multidimensional Scaling (MDS)
Try on 3D spiral structure

@author: Tim Cootes
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Number of samples
ns=60

# Number of dimensions
nd=3

# Generate spiral cone
X=np.zeros([ns,nd])
for i in range(0,ns):
    X[i,0]=i
    X[i,1]=np.sqrt(i)*np.cos(i/3)
    X[i,2]=np.sqrt(i)*np.sin(i/3)
    
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X[:,0],X[:,1],X[:,2])
plt.show()

# PCA
mean=X.mean(0)
cov=np.cov(X,rowvar=False)
eV,P=np.linalg.eigh(cov)
order=np.argsort(-eV)
P2=P[:,[order[0],order[1]]]
b=(X-mean)@P2

plt.figure(figsize=(5,5))
plt.plot(b[:,0],b[:,1],'go')
plt.title("PCA Projection")
plt.show()

### Classical MDS ###

# Compute distance matrix
D=np.zeros((ns,ns))
for i in range(0,ns):
    for j in range(i+1,ns):
        d2=np.sum(np.square(X[i,:]-X[j,:]))
        D[i,j]=d2
        D[j,i]=d2
        
# Construct matrix to do centering
C=np.identity(ns)-np.ones((ns,ns))/ns

B=-0.5*C@D@C

# Use eigh because B should be symmetric
eVals,eVecs=np.linalg.eigh(B)

order=np.argsort(-eVals)

print("Largest eigenvalue: ",eVals[order[0]])

# Pick out eigenvectors for two largest eigenvalues
Y=eVecs[:,[order[0],order[1]]]
Y=Y@np.diag([np.sqrt(eVals[order[0]]),np.sqrt(eVals[order[1]])])

plt.figure(figsize=(5,5))
plt.plot(Y[:,0],Y[:,1],"r+")
plt.title("MDS Mapping")
plt.show()

