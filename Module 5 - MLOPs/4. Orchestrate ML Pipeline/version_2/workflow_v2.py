from typing import Any, Dict, List
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import mlflow
from prefect import task, flow

@task
def load_data(path: str, unwanted_cols: List) -> pd.DataFrame:
    data = pd.read_csv(path)
    data.drop(unwanted_cols, axis=1, inplace=True)
    return data


@task
def get_classes(target_data: pd.Series) -> List[str]:
    return list(target_data.unique())


@task
def get_scaler(data: pd.DataFrame) -> Any:
    # scaling the numerical features
    scaler = StandardScaler()
    scaler.fit(data)
    return scaler


@task
def rescale_data(data: pd.DataFrame, scaler: Any) -> pd.DataFrame:    
    # scaling the numerical features
    # column names are (annoyingly) lost after Scaling
    # (i.e. the dataframe is converted to a numpy ndarray)
    data_rescaled = pd.DataFrame(scaler.transform(data), 
                                columns = data.columns, 
                                index = data.index)
    return data_rescaled


@task
def split_data(input_: pd.DataFrame, output_: pd.Series, test_data_ratio: float) -> Dict[str, Any]:
    X_tr, X_te, y_tr, y_te = train_test_split(input_, output_, test_size=test_data_ratio, random_state=0)
    return {'X_TRAIN': X_tr, 'Y_TRAIN': y_tr, 'X_TEST': X_te, 'Y_TEST': y_te}


@task
def find_best_model(X_train: pd.DataFrame, y_train: pd.Series, estimator: Any, parameters: List) -> Any:
    # Enabling automatic MLflow logging for scikit-learn runs
    mlflow.sklearn.autolog(max_tuning_runs=None)

    with mlflow.start_run():        
        clf = GridSearchCV(
            estimator=estimator, 
            param_grid=parameters, 
            scoring='accuracy',
            cv=5,
            return_train_score=True,
            verbose=1
        )
        clf.fit(X_train, y_train)
        
        # Disabling autologging
        mlflow.sklearn.autolog(disable=True)
        
        return clf


# Workflow
@flow
def main(path: str):
    
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("Iris Species Prediction")
    
    # Define Parameters
    TARGET_COL = 'Species'
    UNWANTED_COLS = ['Id']
    TEST_DATA_RATIO = 0.2
    DATA_PATH = path

    # Load the Data
    dataframe = load_data(path=DATA_PATH, unwanted_cols=UNWANTED_COLS)

    # Identify Target Variable
    target_data = dataframe[TARGET_COL]
    input_data = dataframe.drop([TARGET_COL], axis=1)

    # Get Unique Classes
    classes = get_classes(target_data=target_data)
    
    # Split the Data into Train and Test
    train_test_dict = split_data(input_=input_data, output_=target_data, test_data_ratio=TEST_DATA_RATIO)
    
    # Rescaling Train and Test Data
    scaler = get_scaler(train_test_dict['X_TRAIN'])
    train_test_dict['X_TRAIN'] = rescale_data(data=train_test_dict['X_TRAIN'], scaler=scaler)
    train_test_dict['X_TEST'] = rescale_data(data=train_test_dict['X_TEST'], scaler=scaler)
    
    # Model Training
    ESTIMATOR = KNeighborsClassifier()
    HYPERPARAMETERS = [{'n_neighbors':[i for i in range(1, 51)], 'p':[1, 2]}]
    classifier = find_best_model(train_test_dict['X_TRAIN'], train_test_dict['Y_TRAIN'], ESTIMATOR, HYPERPARAMETERS)
    print(classifier.best_params_)
    print(classifier.score(train_test_dict['X_TEST'], train_test_dict['Y_TEST']))
    
    
# Run the main function
main(path='./data/iris.cv')