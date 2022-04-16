# 1-Dimension Optimisation
# Brent's method

Brent's method is an algorithm of 1-D Optimisation for searching a local minimum in a function. A minimum is bracketed
by three points, a<b<c such that f(b)<f(a) and f(b)<f(c), and then the minimum must be in range [a,c]. Therefore, we 
have to find the decreasing direction and walk one step forward. The extend of this step will impact the speed of convergence.

Golden section search:
- Set an initial bracket [a,b,c]
- Choose new point x in [a,c]
--if x<b, and if f(x)<f(b) then update the interval to [a,x,b] else [x,b,c]
--if x>b, and if f(x)<f(b) then update the interval to [b,x,c] else [a,b,x]
- New interval always smaller
Repeat until interval sufficiently small

Choice of x:
- (1-k)^n * (c-a) = 0.62^n * (c-a)
- k approximate 0.38.

Advantages of Brent’s method:
• 1D optimisation method useful when derivatives not available
• Uses a cunning combination of golden section search and parabolic interpolation
• Fast and reliable

-------------------------------------------------------------------------------------------------------------------------
In my Jupyter Script,

1st Part:
Import Brent's method offered by scipy library.

2nd Part:
Normal method with a fixed step only based on Python.

3ed Part:
Brent's method with step k=0.38 based on Python to find the minimal pont.


