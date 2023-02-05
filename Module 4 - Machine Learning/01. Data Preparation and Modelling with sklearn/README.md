# Introduction to Data Preprocessing and Modelling using SKLearn Library

## Steps for a Machine Learning Project
1. Identify input(X) and output(y) features.
2. Separate the data into X and y.
	- Identify the task by analysing the target variable.
	- For Classification task:
		- Algorithm - Logistic Regression, SVC, KNeighborsClassifier, DecisionTreeClassifier, RandomForestClassifier, GBDTClassifier, etc
		- Evaluation Metric - Accuracy, Confusion Metric, Precision, Recall, ROC AUC, Log Loss, etc
	- For Regression task:
		- Algorithm - Linear Regression, SVC, KNeighborsRegressor, DecisionTreeRegressor, RandomForestRegressor, GBDTRegressor, etc
		- Evaluation Metric - Mean Square Error, Root Mean Square Error, Mean Absolute Error, R Square, Adjusted R Square, etc
3. Split the data(X, y) into training(X_train, y_train) and testing data(X_test, y_test).
4. Apply Data Preprocessing on X_train. Get X_train_transformed.
5. Apply Data Preprocessing on X_test. Get X_test_transformed.
7. Choose an appropriate ML Algorithm. Train a machine learning model using training data (X_train_transformed, y_train).
8. Predict using testing data (X_test_transformed) and get the predictions (y_test_pred).
9. Choose an Evaluation Metric. Using the actual values (y_test) and predictions from model (y_test_pred), get the score.

## Data Preprocessing (Data Cleaning + Data Transformation)
1. Numerical Data Transformation Techniques
	- Standardization
	- Normalization
2. Categorical Data Transformation Techniques
	- One Hot Encoding or Dummy Encoding
	- Label Encoding
3. Text Data Transformation Techniques
	- Bag of Words
	- Term Frequency Inverse Document Frequency (TF IDF)
	- Word2Vec
	- GloVe
	- FastText
	- Embeddings from Language Models (ELMo)
	- Bidirectional Encoder Representation from Transformers (BERT)
4. Image Data Transformation Techniques
	- Flattening
	- Convolutional Neural Network + Flattening
		- VGGNet
		- AlexNet
		- Inception Module (GoogleNet)
		- ResNet
		- MobileNet
		- EfficientNet
	- VisionTransformers
5. Audio Data Transformation Techniques
	- Mel Scaled Filter Bank
	- Mel Frequency Cepstral Coefficients (MFCC)

## SKLearn Implementation
1. Installing sklearn.
	```python
	! pip install -U scikit-learn
	```  
	
	```python
	import sklearn
	print(sklearn.__version__)
	```
2. Splitting the data into train and test.
	```python
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=100)	
	```
3. Data Preprocessing on X_train
	- Numerical Feature - Rescaling using Standardization
	```python
	# scaling the numerical features
	from sklearn.preprocessing import StandardScaler
	
	# Creating object of StandardScaler class
	scaler = StandardScaler()

	# column names are (annoyingly) lost after Scaling
	# (i.e. the dataframe is converted to a numpy ndarray)
	X_train_transformed = pd.DataFrame(scaler.fit_transform(X_train), 
										columns = X_train.columns, 
										index = X_train.index)

	X_train_transformed.head()
	```
	- Numerical Feature - Rescaling using Normalization
	```python
	# scaling the numerical features
	from sklearn.preprocessing import MinMaxScaler
	
	# Creating object of MinMaxScaler class
	scaler = MinMaxScaler()

	# column names are (annoyingly) lost after Scaling
	# (i.e. the dataframe is converted to a numpy ndarray)
	X_train_transformed = pd.DataFrame(scaler.fit_transform(X_train), 
										columns = X_train.columns, 
										index = X_train.index)

	X_train_transformed.head()
	```
	- Categorical Feature - Encoding using OneHotEncoder
	```python
	# OneHotEncoding the categorical features
	from sklearn.preprocessing import OneHotEncoder
	
	# Creating object of OneHotEncoder
	encoder = OneHotEncoder(drop='first', sparse=False)

	# column names are (annoyingly) lost after OneHotEncoding
	# (i.e. the dataframe is converted to a numpy ndarray)
	X_train_transformed = pd.DataFrame(encoder.fit_transform(X_train), 
								   columns=encoder.get_feature_names_out(X_train.columns), 
								   index = X_train.index)

	X_train_transformed.head()
	```
4. Data Preprocessing on X_test.
	- Numerical Features
	```python
	# Use the same 'scaler' object to transform test data
	X_test_transformed = pd.DataFrame(scaler.transform(X_test), 
                                   columns = X_test.columns, 
                                   index = X_test.index)

	X_test_transformed.head()
	```
	- Categorical Features
	```python
	# Use the same 'encoder' object to transform test data
	X_test_transformed = pd.DataFrame(encoder.transform(X_test), 
                                   columns = encoder.get_feature_names_out(X_train.columns), 
                                   index = X_test.index)

	X_test_transformed.head()
	```
5. Training a Model using a Machine Learning Algorithm
	- Regression Task - Linear Regression
	```python
	from sklearn.linear_model import LinearRegression
	regressor = LinearRegression()
	regressor.fit(X_train_transformed, y_train)
	```
	- Classification Task - Logistic Regression
	```python
	from sklearn.linear_model import LogisticRegression
	classifier = LogisticRegression()
	classifier.fit(X_train_transformed, y_train)
	```
6. Predict on the unseen data.
	- Regression Task
	```python
	y_test_pred = regressor.predict(X_test_transformed)
	```
	- Classification Task
	```python
	y_test_pred = classifier.predict(X_test_transformed)
	```
7. Evaluation
	- Regression Task 
	```python
	from sklearn import metrics
	metrics.mean_absolute_error(y_test, y_test_pred)
	```
	- Classification Task
	```python
	from sklearn import metrics
	metrics.accuracy_score(y_test, y_test_pred)
	```