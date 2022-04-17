# Illustration of four local optimisation methods: Powell, Nelder-Mead, Steepes tDescent and Conjugate Gradient methods 

Show path of optimisation steps on a graph.

1. Powell
 
 ![image](https://user-images.githubusercontent.com/26786836/163694773-18871a11-73be-4835-9dd5-77576311d25f.png)![image](https://user-images.githubusercontent.com/26786836/163694776-ecd24274-7f63-46d4-b9d9-d1b4365aface.png)

Number of iterations:  3,              Number of iterations:  73
Result: ( 0.75 , 0.5000000000000003 ), Result: ( 0.5007608233265949 , 0.5043139398692177 )

2. Nelder-Mead

![image](https://user-images.githubusercontent.com/26786836/163694789-e64855bd-f138-44e1-af99-1da73cc6de31.png)![image](https://user-images.githubusercontent.com/26786836/163694795-85d1d232-6982-43aa-bece-52950c965462.png)

Number of iterations:  50 in Quadratic Fn, Result: ( 0.7499794975470762 , 0.5000326539118198 )
                    , 65 in Wiggly Function, Result: ( 0.49999389355157864 , 0.49998900918225914 )

3. Steepes tDescent

![image](https://user-images.githubusercontent.com/26786836/163694807-1244365d-5d89-4bb5-b291-cfec0c3fb7d3.png)

x-grad:  -8.094999999999963
y-grad:  -7.19499999999984
grad_fn:  [-8.1 -7.2]
Result: ( 0.7460427120137126 , 0.5039572879862874 )

4. Conjugate Gradient

![image](https://user-images.githubusercontent.com/26786836/163694816-75457dd8-8ec1-4b0c-b14f-cfd115ab7fa5.png)

x-grad:  -8.59500000000013
y-grad:  -7.594999999999352
grad_fn:  [-8.6 -7.6]
Number of iterations:  2
Result: ( 0.75 , 0.5 
