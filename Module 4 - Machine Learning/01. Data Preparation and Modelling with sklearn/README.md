# Introduction to Data Preprocessing and Modelling using SKLearn Library


<img src="1. Hands-on with sklearn/notes/model_building_pipeline.jpg">


<b>[Click Here](https://model-building-pipeline-tutorial.streamlit.app/) to visualize the step-by-step process of building a Machine Learning model.</b>

## Types of Machine Learning
<ol>
	<li><details>
		<summary><h4>Supervised Learning</h4></summary>
		<ul>
			<li>Classification Task</li>
			<li>Regression Task</li>
		</ul>
		<details>
		<summary><h5>Below Mentioned are the approaches to solve the classification and regression tasks:</h5></summary>
		<ul>
			<li><b>Distance Based Approach:</b> KNeighborsClassifier and KNeighborsRegressor</li>
			<li><b>Rule Based Approach:</b> DecisionTreeClassifier and DecisionTreeRegressor</li>
			<li><b>Probability Based Approach:</b> Naive Bayes for classification</li>
			<li><b>Boundary Based Approach:</b> LogisticRegression and SVC  for classification & LinearRegression for Regression</li>
			<li><b>Ensemble Based Approach:</b> RandomForestClassifier, GBDTClassifier, etc... for Classification & RandomForestRegressor, GBDTRegressor, etc... for Regression</li>
			<li><b>Deep Learning Based Approach:</b> ANN for Classification and ANN for Regression</li>
		</ul>
		</details>
	</details></li>
	<li><details>
		<summary><h4>Unsupervised Learning</h4></summary>
		<ul>
			<li>Clustering Task</li>
			<li>Dimensionality Reduction Task</li>
		</ul>
	</details></li>
	<li><h4>Reinforcement Learning</h4></li>
</ol>


## Model Building Pipeline (Step by Step Procedure)
1. Identify input(X) and output(y) features.
	<ul>
		<li><details>
		<summary>Identifying the Data Preparation Techniques</summary>
			- Identify the data preparation techniques by analysing the input variables (i.e. X).  
			- For Numerical Data  
				- Data Cleaning Steps - Outliers and Missing Values  
				- Feature Engineering Techniques - Standardization and Normalization  
			- For Categorical Data  
				- Data Cleaning Steps - Outliers and Missing Values  
				- Feature Engineering Techniques - One Hot Encoding / Dummy Encoding and Label Encoding  
			- For Text Data  
				- Data Cleaning Steps -  
					a. Removing Special Characters, Punctuations, etc..  
						b. Converting to lower cases  
						c. Removing Stop Words  
						d. Lemmatization / Stemming  
				- Feature Engineering Techniques(Feature Extraction or Vectorization Techniques) - Bag of Words, Term Frequency Inverse Document Frequency (TF IDF), Word2Vec, GloVe, FastText, RNN, LSTMs, GRUs, Embeddings from Language Models (ELMo), Bidirectional Encoder Representation from Transformers (BERT)  
			- For Image Data  
				- Data Cleaning Steps -   
				- Feature Engineering Techniques(Feature Extraction or Vectorization Techniques) - Flattening, Convolutional Neural Network + Flattening (architechtures like: VGGNet, AlexNet, Inception Module (GoogleNet), ResNet, MobileNet, EfficientNet, etc...), VisionTransformers  
			- Audio Data  
				- Data Cleaning Steps -   
				- Feature Engineering Techniques(Feature Extraction or Vectorization Techniques) - Mel Scaled Filter Bank, Mel Frequency Cepstral Coefficients (MFCC)  
		</details></li>
		<li><details>
		<summary>Identifying the supervised ML Task and Evaluation Metric</summary>
			- Identify the task by analysing the target variable (i.e. y).
			- For Classification:
				- Algorithm - Logistic Regression, SVC, KNeighborsClassifier, DecisionTreeClassifier, RandomForestClassifier, GBDTClassifier, etc
				- Evaluation Metric - Accuracy, Confusion Metric, Precision, Recall, ROC AUC, Log Loss, etc
			- For Regression:
				- Algorithm - Linear Regression, SVC, KNeighborsRegressor, DecisionTreeRegressor, RandomForestRegressor, GBDTRegressor, etc
				- Evaluation Metric - Mean Square Error, Root Mean Square Error, Mean Absolute Error, R Square, Adjusted R Square, etc
		</details></li>
	</ul>
4. Split the data(X, y) into training(X_train, y_train) and testing data(X_test, y_test).
5. Apply Data Preprocessing on X_train (which was identified in step-2). Get X_train_transformed.
6. Choose an appropriate ML Algorithm (which was identified in step-3). Train a machine learning model using training data (X_train_transformed, y_train).
7. Apply Data Preprocessing on X_test. Get X_test_transformed.
8. Predict using the ML model on testing data (X_test_transformed) and get the predictions (y_test_pred).
9. Choose an appropriate Evaluation Metric (which was identified in step-3). Using the actual values (y_test) and predictions from model (y_test_pred), get the model's score.

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
