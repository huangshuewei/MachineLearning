# Classification examples

## 1. make blob data
This example is used to generate a set of data. We can use this data to test various classifiers.
It also can generate high-dimension data including 3 or 4 dimension (n_features).

(1) 500 samples with centre at (0, 1) and (3, 3).

![image](https://user-images.githubusercontent.com/26786836/163821487-4871ddc1-04f1-4ccc-99eb-941bcbe3dcea.png)

(2) 500 samples with centre at (0, 1) and (5, 5).

![image](https://user-images.githubusercontent.com/26786836/163821539-5f0f0fb7-f389-4bf8-92d0-d052d1bf3431.png)

(3) 1500 samples with centre at (0, 1) and (5, 5).

![image](https://user-images.githubusercontent.com/26786836/163821604-2aabef17-b14b-4377-b6bf-e500bd4997e4.png)

(3) 1500 samples with centre at (1, 1, 1) and (5, 5, 5). This is 3-dimension data

![image](https://user-images.githubusercontent.com/26786836/163821712-0dafebd3-9879-4cb4-b75e-e97162cf4ea2.png)

----------------------------------------------------------------------------------------------------------------------

## 2. example of LDA & QDA
Example of using linear discriminant analysis and quadratic discriminant analysis for classification.
Apply LDA and QDA functions from sklearn.discriminant_analysis library.

![image](https://user-images.githubusercontent.com/26786836/163823027-fb01b0f0-a3d4-4e37-9d5f-c9f77e582736.png)

(1) 500 samples with centre at (1, 1) and (2, 3) which are classified by LDA method. 

![image](https://user-images.githubusercontent.com/26786836/163823234-2fadff32-66cc-4f43-b3a8-b65995ed75dd.png)
![image](https://user-images.githubusercontent.com/26786836/163823257-ef8b8264-7e52-4026-9b2a-547aa8ac95a4.png)
![image](https://user-images.githubusercontent.com/26786836/163823268-73fc9672-2fdf-43bc-a1a2-b05b0bddc515.png)

Number of positives in training set 250  of  500

Number of true positives 216

Number of false negatives 34

(2) 1000 samples with centre at (4, 3.5) and (4, 4.5) which are classified by LDA method. 

![image](https://user-images.githubusercontent.com/26786836/163823423-a33285bd-6451-472d-9faf-f47ee90ac2b7.png)
![image](https://user-images.githubusercontent.com/26786836/163823433-68deba0a-a7fb-483c-ad32-d2c9bb371725.png)
![image](https://user-images.githubusercontent.com/26786836/163823443-337006a8-08a7-4d18-aae5-376ba5279d1f.png)

Number of positives in training set 500  of  1000

Number of true positives 361

Number of false negatives 139

(3) 1000 samples with centre at (4, 3.5) and (4, 4.5) which are classified by QDA method. 

![image](https://user-images.githubusercontent.com/26786836/163823561-e824a3c4-d891-4989-b4c8-a4c148ac1587.png)
![image](https://user-images.githubusercontent.com/26786836/163823587-74c2eb15-4ed7-4be6-a498-517d79d56eed.png)
![image](https://user-images.githubusercontent.com/26786836/163823601-c59e89b5-c9f1-4f9f-aab0-92eeb852bcfe.png)

Number of positives in training set 500  of  1000

Number of true positives 367

Number of false negatives 133

----------------------------------------------------------------------------------------------------------------------

## 3. random forest method
This function is adopted from sklearn.ensemble (RandomForestClassifier).

![image](https://user-images.githubusercontent.com/26786836/163825479-416a7f27-53c8-4ed5-b799-ea1e8d0f652b.png)

![image](https://user-images.githubusercontent.com/26786836/163825533-21e679f1-ed5c-4e27-936a-9817188255d1.png)

![image](https://user-images.githubusercontent.com/26786836/163825598-b0e7b72e-436c-4d18-b10a-307314b62e54.png)

![image](https://user-images.githubusercontent.com/26786836/163825680-9ff397c1-5809-4251-bd3a-0d875dcb260f.png)







