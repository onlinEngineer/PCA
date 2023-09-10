# PCA
Hand Calculation PCA and Sklearn Calculation Comparision

# Question 1.
In this part, we used sklearn.dataset fetch_olivetti_faces dataset. We used from sklearn import decomposition PCA.

### Data

![image](https://github.com/onlinEngineer/PCA/assets/70773825/a64585d9-9799-4f88-a31a-5b9141322d86)

### Calculated Some Eigenvalues

![image](https://github.com/onlinEngineer/PCA/assets/70773825/1f29d5d9-ddb3-434f-8068-0b9008523e58)


### All Eigenvalues

![image](https://github.com/onlinEngineer/PCA/assets/70773825/ae2a64c2-5c0a-4f44-8827-f02aa9a2ff56)


### Mean Face
![image](https://github.com/onlinEngineer/PCA/assets/70773825/404c6562-f40d-4262-8b1e-77d5ed258b99)

### As an images (Reshaped 64x64)

![image](https://github.com/onlinEngineer/PCA/assets/70773825/3a6f0f6f-ab89-4c3d-88c5-b203bbbc9fe7)

### First 20 Principal Components

![image](https://github.com/onlinEngineer/PCA/assets/70773825/8ead0609-63b9-4789-94fc-d770c2aad0f3)

### As an images (Reshaped 64x64)

![image](https://github.com/onlinEngineer/PCA/assets/70773825/e6ebffa6-1e7e-438e-a537-bde23cfe3833)

### Real Image

![image](https://github.com/onlinEngineer/PCA/assets/70773825/36df258b-aef5-490a-b19a-b08c27acba15)

### As an Image (Reshaped 64x64)

![image](https://github.com/onlinEngineer/PCA/assets/70773825/6e5b1a00-f921-4194-bd78-7a765b920cef)


### PC 5 vs Real (Reshaped 64x64)

![image](https://github.com/onlinEngineer/PCA/assets/70773825/538894d0-7be3-4971-85c5-eabd2659b984)

![image](https://github.com/onlinEngineer/PCA/assets/70773825/99d416fc-57e8-4f30-ba1e-70159f4108d1)![image](https://github.com/onlinEngineer/PCA/assets/70773825/ca7ed9d1-793a-4e2e-88e4-39fdeaa9dd3d)

### PC 10 vs Real (Reshaped 64x64)
![image](https://github.com/onlinEngineer/PCA/assets/70773825/20801bda-0392-4e93-aa4c-1555bcf808a5)

![image](https://github.com/onlinEngineer/PCA/assets/70773825/67133582-33c9-4681-b152-b30ad19d8177)![image](https://github.com/onlinEngineer/PCA/assets/70773825/ecf67a37-b662-4832-9cb8-a678d546b435)

### PC 40 vs Real (Reshaped 64x64)
![image](https://github.com/onlinEngineer/PCA/assets/70773825/2ad6e40a-7e8c-468e-9d7c-40d1ef90025e)
![image](https://github.com/onlinEngineer/PCA/assets/70773825/ce177d37-63ff-43fe-a7bc-84cf4939b1c6)![image](https://github.com/onlinEngineer/PCA/assets/70773825/8465d7e6-8dd4-4a1d-a5fe-565a9b41558c)

### PC 200 vs Real (Reshaped 64x64)
![image](https://github.com/onlinEngineer/PCA/assets/70773825/c2792462-7ea8-4a00-8a18-0507eaa54291)

![image](https://github.com/onlinEngineer/PCA/assets/70773825/652324ba-35c0-4c23-8898-8cd8fba64943)![image](https://github.com/onlinEngineer/PCA/assets/70773825/e55a4665-8f5d-43d0-9b6c-e6eef94c0f68)

## First 3 Principal Components (3d)

### First Principal Components (First 100)
![image](https://github.com/onlinEngineer/PCA/assets/70773825/062a6df1-6306-4e33-ae7b-b3c0806b2058)

### Second Principal Components (First 100)


### Third Principal Components (First 100)


## 3D Graph of First 3 Principal Components

# Question 2.






# CONCLUSION
In this assignment, we talked about what is PCA, how can we apply pca, what is the main charectistic of a PCA etc.
Principal Component Analysis, or PCA, is a dimensionality reduction method commonly used to reduce the dimensionality of large datasets by transforming data with a large set of variables into a smaller variable that contains nearly all of the information in the large set.
In question 1, we used fetch olivetti dataset to reduction of dimention of this dataset. When we reduce the dimention, the pictures are getting blurry and the pixels are starting to get the same colors. For example, a picture with 5 components has 5 colors, while a picture with 40 components has 40 different colors. Therefore, the lower the color, the more difficult it is to select the photo. However, as seen in the examples, it is not necessary to include many colors in order to select photos. If the correct number of components is found, the pca process can be applied and the correct result can be achieved more easily.
In question 2, we calculated the numbers by hand. To calculate the covariance, firstly we get the mean of the data and after that, we subtract the data values from mean and multiply with the transpose of it. Thanks to covariance matrix, we can calculate the eigenvalues by subracting from lambda matrix. Lambda matrix is an unit matrix. After these calculation, the lambda will have two different values because of second degree equation. After calculation eigenvalues, we can calculate eigenvectors with multiply by coveriance matrix some unknown values and make the equation equal to lambda values. These result will have our first and second principal components.
