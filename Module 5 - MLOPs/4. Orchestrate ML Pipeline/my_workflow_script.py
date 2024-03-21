import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn import metrics

from prefect import task, flow

@task
def load_data(file_path):
    """
    Load data from a CSV file.
    """
    return pd.read_csv(file_path)


@task
def split_inputs_output(data, inputs, output):
    """
    Split features and target variables.
    """
    X = data[inputs]
    y = data[output]
    return X, y
	

@task
def split_train_test(X, y, test_size=0.25, random_state=0):
    """
    Split data into train and test sets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
	
	
@task
def preprocess_data(X_train, X_test, y_train, y_test):
    """
    Rescale the data.
    """
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test
	

@task
def train_model(X_train_scaled, y_train, hyperparameters):
    """
    Training the machine learning model.
    """
    clf = KNeighborsClassifier(**hyperparameters)
    clf.fit(X_train_scaled, y_train)
    return clf
	

@task
def evaluate_model(model, X_train_scaled, y_train, X_test_scaled, y_test):
    """
    Evaluating the model.
    """
    y_train_pred = model.predict(X_train_scaled)
    y_test_pred = model.predict(X_test_scaled)

    train_score = metrics.accuracy_score(y_train, y_train_pred)
    test_score = metrics.accuracy_score(y_test, y_test_pred)
    
    return train_score, test_score


# Workflow
@flow(name="KNN Training Flow")
def workflow():
    DATA_PATH = "data/iris.csv"
    INPUTS = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    OUTPUT = 'Species'
    HYPERPARAMETERS = {'n_neighbors': 3, 'p': 2}
    
    # Load data
    iris = load_data(DATA_PATH)

    # Identify Inputs and Output
    X, y = split_inputs_output(iris, INPUTS, OUTPUT)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    # Preprocess the data
    X_train_scaled, X_test_scaled, y_train, y_test = preprocess_data(X_train, X_test, y_train, y_test)

    # Build a model
    model = train_model(X_train_scaled, y_train, HYPERPARAMETERS)
    
    # Evaluation
    train_score, test_score = evaluate_model(model, X_train_scaled, y_train, X_test_scaled, y_test)
    
    print("Train Score:", train_score)
    print("Test Score:", test_score)



if __name__ == "__main__":
    workflow.serve(
        name="my-first-deployment",
        cron="* * * * *"
    )