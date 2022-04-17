# 2-D optimisaton method with constraint.

## Differentiate function and apply constrainted optimisaton method.
### 1. use Sympy library to compute differentiate function

#### Differentiate function exp(2x+1)
2*exp(2*x + 1)

#### Differentiate function sin(exp(ax))
a*exp(a*x)*cos(exp(a*x))

#### Differentiate function b*cos(exp(ax)+c)
-a*b*exp(a*x)*sin(c + exp(a*x))

#### Differentiate function log(ax+by+c)
df/dx= a/(a*x + b*y + c)
df/dy= b/(a*x + b*y + c)


### 2. find the minimum of f(x,y)=cos⁡(e^(-(x-2)^2 )+x(y-1)^2) subject to the constraint that the solution must be within 0.3 of the point (1,2).

res=minimize(constraint_fxy...
             ,constraint_centre...
             ,method='Nelder-Mead'...
             ,callback=record_result)

Number of iterations:  33

Number of function evaluations:  67

Result: ( 1.126142887551396 , 2.2721900019736503 )

![image](https://user-images.githubusercontent.com/26786836/163724006-b2ca5331-5547-41f9-976d-b163bd2cec62.png)

