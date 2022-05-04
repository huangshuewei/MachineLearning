# -*- coding: utf-8 -*-
"""
Example of building an autoencoder as a multi-layer
perceptron in PyTorch.

"""

import torch
from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import torch.optim as optim
import time

# Number of samples
n_samples=100

# Number of dimensions
nd=3

# Generate spiral cone
X=np.zeros([n_samples,nd])
for i in range(0,n_samples):
    X[i,0]=i
    X[i,1]=np.sqrt(i)*np.cos(i/9)
    X[i,2]=np.sqrt(i)*np.sin(i/9)
    
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X[:,0],X[:,1],X[:,2])
plt.show()


Xt=torch.tensor(X,dtype=torch.float32)

N_hidden=20  # Number of dimensions of hidden layer

# Use the nn package to define a model as a sequence of layers. 
# nn.Sequential is a Module which contains other Modules, 
# and applies them in sequence to produce its output. 
# Each Linear Module computes output from input using a
# linear function, and holds internal Tensors for its weight and bias.
model = torch.nn.Sequential(
    torch.nn.Linear(nd, N_hidden),
    torch.nn.Sigmoid(),
    torch.nn.Linear(N_hidden, 1),
    torch.nn.Linear(1, N_hidden),
    torch.nn.Sigmoid(),
    torch.nn.Linear(N_hidden,nd)
)

def init_weights(m):
    if isinstance(m, torch.nn.Linear):
        m.weight.data.uniform_(-1,1)
        m.bias.data.fill_(0.01)

model.apply(init_weights)

loss_fn = torch.nn.MSELoss()

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# Number of samples per batch
# Must divide number of samples exactly
batch_size=25

# Number of complete passes through all data
n_epochs=15000

# Create a random number generator to make permutations
#rng=np.random.default_rng()

start_time=time.perf_counter()

for ep in range(n_epochs):
    # Randomly permute the data so it is presented
    # in a different order in each epoch
    perm=np.random.permutation(n_samples)
    
    # Total loss is sum over all batches
    total_loss=0
    
    for b in range(round(n_samples/batch_size)):
        # Pick out the b-th chunk of the data
        batch_perm=perm[b*batch_size:(b+1)*batch_size]
        y_pred = model(Xt[batch_perm])
    
        loss = loss_fn(y_pred, Xt[batch_perm])
        total_loss+=loss.item()
   
        # Zero the gradients before running the backward pass.
        model.zero_grad()
    
        # Compute gradients. 
        loss.backward()
    
        # Use the optimizer to update the weights
        optimizer.step()
            
    if ((ep+1)%100==0):  # Print every 100th epoch
        print(ep+1, total_loss)
 
end_time=time.perf_counter()
print("Total time spent optimizing: {:0.1f}sec.".format(end_time-start_time))

# Apply model to whole set
y_pred=model(Xt)
Y=y_pred.detach().numpy()
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X[:,0],X[:,1],X[:,2],color='green')
ax.plot(Y[:,0],Y[:,1],Y[:,2],color='red')
plt.show()

# To encode, use first modules in model:
y=model[0:3](Xt)

# To decode use the rest:
x_new=model[3:](y)
