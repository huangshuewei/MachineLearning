# -*- coding: utf-8 -*-
"""
Example of building a Multi-layer Perceptron with PyTorch
Shows how to use optimizer to simplify steps

"""

import torch
from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import time

# Display contour plot of f at all points (x[i],y[j])
def contour_plot1(x,y,f,n_levels):
    xx, yy = np.meshgrid(x, y)
    p=np.hstack([xx.reshape(-1,1),yy.reshape(-1,1)])
    X=torch.tensor(p,dtype=torch.float32)
    fp=f(X)
    z=fp.reshape(xx.shape).detach().numpy()
    plt.contourf(x,y,z,n_levels)


Xnp, ynp = make_blobs(n_samples=150, centers = [(1, 1), (5, 3), (7, 1)], n_features=2)
ynp[ynp==2]=0 # Blob2 relabelled as 0

X=torch.tensor(Xnp,dtype=torch.float32)
y=torch.tensor(ynp[:,np.newaxis],dtype=torch.float32)

N_hidden=10  # Number of dimensions of hidden layer

# Use the nn package to define a model as a sequence of layers. 
# nn.Sequential is a Module which contains other Modules, 
# and applies them in sequence to produce its output. 
# Each Linear Module computes output from input using a
# linear function, and holds internal Tensors for its weight and bias.
model = torch.nn.Sequential(
    torch.nn.Linear(2, N_hidden),
    torch.nn.Sigmoid(),
    torch.nn.Linear(N_hidden, 1),
    torch.nn.Sigmoid()
)

# Use Binary Cross Entropy as loss function.
loss_fn = torch.nn.BCELoss()

# Define optimizer and show it the parameters
learning_rate=0.001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

n_its=5000  # Number of iterations

start_time=time.perf_counter()

for t in range(n_its):
    y_pred = model(X)

    loss = loss_fn(y_pred, y)
    if ((t+1)%200==0):  # Print every 200th result
        print(t+1, loss.item())

    # Zero the gradients before running the backward pass.
    model.zero_grad()

    # Backward pass: compute gradient of the loss with respect to all the learnable
    # parameters of the model. 
    loss.backward()

    # Use the optimizer to update the weights
    optimizer.step()
         
end_time=time.perf_counter()
print("Total time spent optimizing: {:0.1f}sec.".format(end_time-start_time))

# Create a grid of points
px = np.arange(Xnp[:,0].min()-0.5, Xnp[:,0].max()+0.5, 0.1)
py = np.arange(Xnp[:,1].min()-0.5, Xnp[:,1].max()+0.5, 0.1)


# Use different colours for different classes
X0=Xnp[ynp==0] # Select samples for class 0
X1=Xnp[ynp==1] # Select samples for class 1
plt.plot(X0[:,0],X0[:,1],"+",color="red")
plt.plot(X1[:,0],X1[:,1],"o",color="green")
contour_plot1(px,py,model,15)
