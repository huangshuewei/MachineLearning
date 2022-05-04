# -*- coding: utf-8 -*-
"""
Example of classical Multidimensional Scaling (MDS)
Experiment with centres at +/-3e_i where e_i are the 
axis vectors.

@author: Tim Cootes
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs

# Number of samples
ns=500

s=9 # Separation of centres
blob_c=np.array([[0,0,0,0],
                 [s,0,0,0],[-s,0,0,0],
                 [0,s,0,0],[0,-s,0,0],
                 [0,0,s,0],[0,0,-s,0],
                 [0,0,0,s],[0,0,0,-s]])

# Generate samples from n blobs
# Each row of X is one sample
X, y = make_blobs(n_samples=ns, centers = blob_c)

# PCA
mean=X.mean(0)
cov=np.cov(X,rowvar=False)
eV,P=np.linalg.eigh(cov)
order=np.argsort(-eV)
P2=P[:,[order[0],order[1]]]
b=(X-mean)@P2

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

plt.plot(Y[:,0],Y[:,1],"r+")
plt.title("MDS Mapping")
plt.show()

