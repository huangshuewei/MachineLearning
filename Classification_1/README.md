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

### (1) 500 samples with centre at (1, 1) and (4, 5) which are classified by random forest method. 

#### n_estimators=1, max_depth=3, min_samples_leaf=2

![image](https://user-images.githubusercontent.com/26786836/163826154-c1e3f26e-975a-4f39-9e3c-ad99bc093e9f.png)
![image](https://user-images.githubusercontent.com/26786836/163826181-65f1b857-ada0-4bca-932d-2ee8ad4c7105.png)
![image](https://user-images.githubusercontent.com/26786836/163826211-5c82e370-3d0f-4e52-8fe8-0355515e92f7.png)

Number of positives in training set 250  of  500

Number of true positives 248

Number of false negatives 2

### (2) 500 samples with centre at (1, 1) and (4, 5) which are classified by random forest method. 

#### n_estimators=1, max_depth=5, min_samples_leaf=2

#### Change the max_depth

Number of positives in training set 250  of  500

Number of true positives 248

Number of false negatives 2

![image](https://user-images.githubusercontent.com/26786836/163827022-e4c17414-7cf8-48a6-8250-9e0223a9ef6f.png)
![image](https://user-images.githubusercontent.com/26786836/163827036-f9a7288e-b747-4396-bf17-87d12e4d6df6.png)

### (3) 500 samples with centre at (1, 1) and (4, 5) which are classified by random forest method. 

#### ""n_estimators=4"", max_depth=3, min_samples_leaf=2

#### Change the number of trees (n_estimators)

Number of positives in training set 250  of  500

Number of true positives 249

Number of false negatives 1

![image](https://user-images.githubusercontent.com/26786836/163827343-0a6dcb03-7152-418e-a52b-11337a3c8217.png)
![image](https://user-images.githubusercontent.com/26786836/163827358-09815f1b-3e4b-4cfe-b936-9bc43717d314.png)

### (3) 500 samples with centre at (1, 1) and (4, 5) which are classified by random forest method. 

#### n_estimators=4, ""max_depth=5"", min_samples_leaf=2

#### Change the depth of trees (max_depth)

Number of positives in training set 250  of  500

Number of true positives 248

Number of false negatives 2

![image](https://user-images.githubusercontent.com/26786836/163828039-66ca2f63-1924-4a2a-a4fd-e5ae4a232465.png)
![image](https://user-images.githubusercontent.com/26786836/163828043-567b8acb-c743-418a-9191-6c1e9f2f2992.png)

### (4) 500 samples with centre at (1, 1) and (6, 6) which are classified by random forest method. 

#### n_estimators=1, max_depth=3, min_samples_leaf=2

#### Move the centres apart together 

Number of positives in training set 250  of  500

Number of true positives 250

Number of false negatives 0

![image](https://user-images.githubusercontent.com/26786836/163828897-96fbacf6-b9c2-428c-a0f6-0777a5220e5e.png)
![image](https://user-images.githubusercontent.com/26786836/163828913-6dd5ff8e-e78b-4158-a71c-508c8d7b2e06.png)

### (4) 500 samples with centre at (2, 2) and (3, 3) which are classified by random forest method. 

#### n_estimators=1, max_depth=3, min_samples_leaf=2

#### Move the centres apart together 

Number of positives in training set 250  of  500

Number of true positives 165

Number of false negatives 85

![image](https://user-images.githubusercontent.com/26786836/163829036-64acdc20-86a2-44b3-bd5f-bd764abda1e4.png)
![image](https://user-images.githubusercontent.com/26786836/163829045-f733ede2-7a05-4c82-8fa3-5fb11471ee86.png)

### (5) 1000 samples with centre at (1, 1) and (4, 5) which are classified by random forest method. 

#### Increase the number of samples

Number of positives in training set 500  of  1000

Number of true positives 494

Number of false negatives 6

![image](https://user-images.githubusercontent.com/26786836/163829234-8c754da2-fa04-4a62-9613-ad8104477b5c.png)

----------------------------------------------------------------------------------------------------------------------
## 4. quadratic classifier and ROC analysis of this classifier
In order to test this classifier, ROC analysis is a common and widespread method to assess classifiers.
### Likeliood ratio

![image](https://user-images.githubusercontent.com/26786836/163831130-1bc68c2a-9b93-4084-999c-521d1f40fcb8.png)

![image](https://user-images.githubusercontent.com/26786836/163831190-f4a08560-d5a8-4ca9-8106-d61e5e47956f.png)

![image](https://user-images.githubusercontent.com/26786836/163831223-f30fecc3-e3a1-4cb3-9429-e72e72e59222.png)

### (1) reading from the file.
These data are divided in to train and test.
Compute mean values and covariance matrix of train data.

### (2) use training data to generate likelihood ratio model.
Compute likelihood ratio model trained by mean values and covariance matrix of train data.

### (3) define a threshold t to scan likelihood ratio.
This threshold is a set of numbers between -10 and 10.

### (4) calculate True and False positives.
Based on each threshold to compute True and False positives and then plot sensitivity and specifility.

![image](https://user-images.githubusercontent.com/26786836/163832135-73efe37c-c974-4171-b801-c9539e1aeb37.png)

