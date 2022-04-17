# Examples

### 1.adding flat distribution
This example shows a distribution with different number of dices and n times.
The first figure and the second figure illustrate flat distributions.
Increasing n times is able to get flatter distribution.

![image](https://user-images.githubusercontent.com/26786836/163720483-ea56da9d-a101-4ab4-b874-732ab167af69.png)![image](https://user-images.githubusercontent.com/26786836/163720540-633f7770-ed18-425a-a550-8731327f4cf6.png)

Increasing the number of dices and n times, the distribution can reach a normal distribution.

![image](https://user-images.githubusercontent.com/26786836/163720650-16ff1a94-be9a-4097-b5e8-2ea1ef5fa02a.png)![image](https://user-images.githubusercontent.com/26786836/163720655-d1731db9-0761-43f0-9c1b-cda23ca23710.png)

---------------------------------------------------------------------------------------------------------------------------------------------

### 2.fit normal distribution
This example depicts the usage of estimating mean value and covariance matrix.

1st step: set a initial mean value and a covariance matrix to build a probability distribution.

Mean:
 [1 2]
Covariance:
 [[ 2.53204066 -0.3759543 ]
 [-0.3759543   0.48631186]]
 
 ![image](https://user-images.githubusercontent.com/26786836/163721103-ce1995f2-60d0-4c13-80ba-af0248818d52.png)


2nd step: extract 1000 points in this distribution and estimate the mean value and covariance.

Estimate of mean:  [1.04101961 1.97491363]
Estimate of cov:
 [[ 2.50616793 -0.39144079]
 [-0.39144079  0.47774513]]
Eigenvalues of covar:  [2.57908608 0.40482698]

---------------------------------------------------------------------------------------------------------------------------------------------
