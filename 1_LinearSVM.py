# -*- coding: utf-8 -*-
"""
Simple example of linear Support Vector Machine
"""

from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt

# Display contour plot of f at all points (x[i],y[j])
def contour_plot1(x,y,f,n_levels):
    xx, yy = np.meshgrid(x, y)
    p=np.hstack([xx.reshape(-1,1),yy.reshape(-1,1)])
    fp=f(p)
    plt.contourf(x,y,fp.reshape(xx.shape),n_levels)


X, y = make_blobs(n_samples=100, centers = [(1, 3), (5, 3)], n_features=2)


clf = LinearSVC(random_state=0, tol=1e-5)
clf.fit(X, y)
LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=1e-05, verbose=0)

print(clf.coef_)
print(clf.intercept_)
print(clf.predict([[0, 0]]))

# Create a grid of points
px = np.arange(X[:,0].min(), X[:,0].max(), 0.1)
py = np.arange(X[:,1].min(), X[:,1].max(), 0.1)


# Use different colours for different classes
X0=X[y==0] # Select samples for class 0
X1=X[y==1] # Select samples for class 1
plt.plot(X0[:,0],X0[:,1],"+",color="red")
plt.plot(X1[:,0],X1[:,1],"o",color="green")
contour_plot1(px,py,clf.predict,15)
plt.title("Estimated class at each point")
plt.show()
