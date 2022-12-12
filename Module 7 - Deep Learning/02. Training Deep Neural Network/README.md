# Training a Deep Neural Network

## Training a Single Neuron
**Training a network means finding the best edge weights.**
This is achieved by feed forwarding a data point and then back propogating using chain rule of derivation. While back propogating update the edge weights.

## Regularization
Neural Networks have a large architecture (i.e. weights and biases) hence they have a tendency to overfit easily. We can apply regularization to get rid of this problem.
1. Add a regularization term to the loss function.
	- Lasso Regularization
	- Ridge Regularization
2. Dropouts
	- Randomly remove some interconnections.
	- Never apply dropout on output layer.
3. BatchNormalization

## How to train a Deep Neural Network?
1. Preprocess the data. 
2. Input Layer - Depends on the number of features in input data.
3. Hidden Layers
	- Choose an activation function 
		- Sigmoid
		- Tanh
		- ReLU
	- Randomly initialize the weights.
		- Glorot - If activation function is Sigmoid or Tanh.
		- He - If activation function is ReLU.
	- Regularization.
		- Add BatchNormalization.
		- Add Dropout with dropout rate.
4. Output Layer
	- For Classification
		- Number of Neurons = Number of classes
		- Activation - Softmax Activation
		- Loss - Categorical Cross Entropy
		- Metric - Accuracy
		- Optimizer - Adam
	- For Regression
		- Number of Neurons = 1
		- Activation - Linear Activation
		- Loss - Mean Squared Error
		- Metric - MSE, MAE, etc
		- Optimizer - Adam
5. Hyperparameters
	- Number of layers
	- Number of neurons in each layers
	- Dropout rate
	
## Keras Implementation
1. Define the model.
	- For Classification
		```python
		model = Sequential()
		model.add(Dense(10, input_dim=784, activation='softmax'))
		```  
	- For Classification - Another Example	
		```python
		model = Sequential()
		# FC - 512
		model_relu.add(Dense(512, input_dim=784, activation='relu', kernel_initializer='he_normal'))
		model_relu.add(BatchNormalization())
		model_relu.add(Dropout(0.3))
		
		# FC - 128
		model_relu.add(Dense(128, activation='relu', kernel_initializer='he_normal'))
		model_relu.add(BatchNormalization())
		model_relu.add(Dropout(0.3))

		# FC - 10
		model.add(Dense(10, activation='softmax'))
		```
	- For Regression
		```python
		model = Sequential()
		model.add(Dense(1, input_dim=784, activation='linear'))
		```
2. Compile the model.
	- For Classification
		```python
		model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
		```
	- For Regression
		```python
		model.compile(optimizer='adam', loss='mse', metrics=['mae'])
		```
3. Fit the model.
	```python
	model.fit(X_train, y_train, batch_size=128, epochs=10)
	```
4. Predict and evaluate.
	```python
	model.evaluate(X_test, y_test, verbose=0)
	```