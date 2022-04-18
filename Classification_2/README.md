# Support Vector machine
Support Vector machine can be divided into two classes, linear SVM and non-linear SVM.

## (1) LinearSVM
LinearSVM function used in this practice is from sklearn library.

![image](https://user-images.githubusercontent.com/26786836/163868953-ba098715-72a4-455f-ba25-5977b2058cda.png)

## (2) NonlinearSVM
NonlinearSVM has two different kernals utilised in this practice.

### 1. kernel='rbf'
Number of support vectors:  40

![image](https://user-images.githubusercontent.com/26786836/163869385-cd415671-6087-4600-8564-97cbdce875d3.png)

### 2. kernel='poly',degree=2
Number of support vectors:  25

![image](https://user-images.githubusercontent.com/26786836/163869504-539c2841-6a3f-47a7-b731-89284cbbef3c.png)

### 3. kernel='poly',degree=4
Number of support vectors:  15

![image](https://user-images.githubusercontent.com/26786836/163869556-bc885e6c-5a19-4994-9035-b71f6a7a26ab.png)

-------------------------------------------------------------------------------------------------------------------
# Simple perceptron
This simple perceptron has two inputs and one output.
Two inputs are linear ombination and the output is computed by Sigmoid activation function.
The weights are trained by Backward pass and the loss is calculated via Binary Cross Entropy as loss function.
Weights will be updated 5000 times.

![image](https://user-images.githubusercontent.com/26786836/163870686-598c665c-b218-499a-b988-702d37d5a722.png)

-------------------------------------------------------------------------------------------------------------------
# Model fitting
In this case, I compare two different Cost Functions. Optimisation method is Powell.

![image](https://user-images.githubusercontent.com/26786836/163871176-f2d24ecc-f728-41ac-b58e-5ad54b7bb22b.png)

### (1) Show data in one image.

![image](https://user-images.githubusercontent.com/26786836/163871539-6e3e02fd-cd0d-4648-ac45-078d1a5918f6.png)

### (2) Show the result of model fitting via d**2 and abs(d)

![image](https://user-images.githubusercontent.com/26786836/163871893-09bcc234-dc0c-46a0-ae30-576226fa8fe1.png)
![image](https://user-images.githubusercontent.com/26786836/163871908-f682122f-fa5b-4c45-ab1a-7159f8f90b51.png)

![image](https://user-images.githubusercontent.com/26786836/163871983-adf3cc0d-e5bf-4997-a866-1e549b13f2ba.png)
