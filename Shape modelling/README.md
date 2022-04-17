# Shape modelling and Principal component analysis (PCA).

## 1. Show points
Import data from pelvis_shapes(2).txt, which has 12 points in each shape.

##### Number of shapes 596; Number of points 12

Illustrates one shape and all shapes below.

![image](https://user-images.githubusercontent.com/26786836/163731836-dc6d4efb-5e28-4518-86a1-3d7fab9056c0.png)![image](https://user-images.githubusercontent.com/26786836/163731840-36a780d5-daa0-46d5-aaa2-1e1e8d5aad97.png)


## 2. Build shape mode
Import data from pelvis_shapes(2).txt, which has 12 points in each shape.
Compute the mean shape of 596 pelvis shapes.

![image](https://user-images.githubusercontent.com/26786836/163733253-d80b4558-3ef4-46d9-8fec-920d0d07e091.png)

Compute eigenvalues and sort all eigenvalues.
Sort by the eigenvalues (largest first)

![image](https://user-images.githubusercontent.com/26786836/163733343-e9c0cf87-742a-4a8c-a6c5-5b72e39641cd.png)

Create a model with t modes. Here t is 3 meaning three largest eigenvalues.
Generate shape with +/- SD

![image](https://user-images.githubusercontent.com/26786836/163733491-5d2c8af4-eb03-4284-afad-e2ef33ef5e46.png)

Show shapes with the first mode +/- SD.

![image](https://user-images.githubusercontent.com/26786836/163733623-ba5e0587-4674-4bef-9413-c401e74d670b.png)

Extract parameters for all shapes. Show 2 parameters (Dimension) and 3 parameters (Dimension)

![image](https://user-images.githubusercontent.com/26786836/163733655-b01d3c98-c05b-4ae2-8d05-27cb2be1d85e.png)
![image](https://user-images.githubusercontent.com/26786836/163733659-933ae93c-506e-4af0-9988-bda6223abc1b.png)

## 3. Shape modelling task and PCA task
### Shape Modelling Tasks
This part is similar to the last one, Build shape mode.
The difference is that I show shape modelling with three largest eigenvalues.

![image](https://user-images.githubusercontent.com/26786836/163734073-5765b283-723d-46d8-8f89-aa1ca4a884f2.png)

![image](https://user-images.githubusercontent.com/26786836/163734159-d27a583f-aee1-42fb-9d62-11030007a422.png) ![image](https://user-images.githubusercontent.com/26786836/163734166-1303e10f-9b67-41e2-ba1e-fc3cb622626c.png) ![image](https://user-images.githubusercontent.com/26786836/163734177-706e3d9b-4e6c-4573-acd9-ae4e8a17c6c2.png)

Then conducting dimensionality reduction from 12 to 3 shape parameters.
Plot the Histograms in each domain.

![image](https://user-images.githubusercontent.com/26786836/163734273-887afa1a-f593-48f1-b730-b4ce0233e237.png)
![image](https://user-images.githubusercontent.com/26786836/163734275-9c5e1421-2ec6-41df-809d-911441bab380.png)
![image](https://user-images.githubusercontent.com/26786836/163734277-c3f3e23d-344e-49b4-ae8a-a40d811f1828.png)

### PCA Task
A simple example of PCA used to reduce dimension of data.
1. Load PCA_data1.txt
2. Show first 2 data in figure.

![image](https://user-images.githubusercontent.com/26786836/163734582-afa5bd5e-4a21-40b5-93f7-f0d0213d6a70.png)

3. Calculate the eigenvectors and eigenvalues and Sort by the eigenvalues (largest first)

![image](https://user-images.githubusercontent.com/26786836/163734622-a2d481c5-f45c-44f8-a7fe-f9819eaf61ce.png)

4. Projection of the data onto the first two dimensions

P_PCA has shape (10, 2)

The estimation of the number of dimension is  2

D_PCA_data has shape (200, 10)

B_PCA has shape (2, 200)

![image](https://user-images.githubusercontent.com/26786836/163734771-f04f1ef9-dce2-44d6-8e91-86ca9d07a12b.png)


