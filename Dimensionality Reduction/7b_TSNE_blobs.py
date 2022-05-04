# -*- coding: utf-8 -*-
"""
t-SNE examples - Multiple blobs

@author: Tim Cootes
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.datasets.samples_generator import make_blobs
from mpl_toolkits.mplot3d import Axes3D

from sklearn.manifold import TSNE

# Generate samples at +/s from origin in each dimension
# Number of samples
ns=1000


s=5 # Separation of centres
blob_c=np.array([[0,0,0,0],
                 [s,0,0,0],[-s,0,0,0],
                 [0,s,0,0],[0,-s,0,0],
                 [0,0,s,0],[0,0,-s,0],
                 [0,0,0,s],[0,0,0,-s]])

# Generate samples from n blobs
# Each row of X is one sample
X, y = make_blobs(n_samples=ns, centers = blob_c)


# PCA projection for comparison
mean=X.mean(0)
cov=np.cov(X,rowvar=False)
eV,P=np.linalg.eigh(cov)
order=np.argsort(-eV)
P2=P[:,[order[0],order[1]]]
b=(X-mean)@P2



plt.figure(figsize=(5,5))
plt.scatter(b[:,0],b[:,1])
plt.title("PCA Projection")
plt.show()

embedding = TSNE(n_components=2,perplexity=10)
z = embedding.fit_transform(X)

plt.figure(figsize=(5,5))
plt.scatter(z[:,0],z[:,1])
plt.title("t-SNE Embedding of multiple blobs")
plt.show()

