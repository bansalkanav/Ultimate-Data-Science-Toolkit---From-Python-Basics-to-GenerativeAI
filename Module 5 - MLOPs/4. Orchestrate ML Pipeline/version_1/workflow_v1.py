from typing import Any, Dict, List
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(path: str, unwanted_cols: List) -> pd.DataFrame:
    data = pd.read_csv(path)
    data.drop(unwanted_cols, axis=1, inplace=True)
    return data


def get_classes(target_data: np.array) -> List[str]:
    return list(target_data.unique())


def rescale_numerical_columns(data: pd.DataFrame) -> pd.DataFrame:
    # scaling the numerical features
    scaler = StandardScaler()

    # column names are (annoyingly) lost after Scaling
    # (i.e. the dataframe is converted to a numpy ndarray)
    data_rescaled = pd.DataFrame(scaler.fit_transform(data), 
                                        columns = data.columns, 
                                        index = data.index)

    return data_rescaled


def split_data(input_: pd.DataFrame, output_: pd.Series, test_data_ratio: float) -> Dict[str, Any]:
       
    X_tr, X_te, y_tr, y_te = train_test_split(input_, output_, test_size=test_data_ratio, random_state=0)
    
    return {'X_TRAIN': X_tr, 'Y_TRAIN': y_tr, 'X_TEST': X_te, 'Y_TEST': y_te}


def main():
    # Define Parameters
    TARGET_COL = 'Species'
    UNWANTED_COLS = ['Id']
    TEST_DATA_RATIO = 0.2
    DATA_PATH = './data/iris.csv'

    # Run Functions
    dataframe = load_data(path=DATA_PATH, unwanted_cols=UNWANTED_COLS)

    # Workflow
    target_data = dataframe[TARGET_COL]
    input_data = dataframe.drop([TARGET_COL], axis=1)

    numerical_data = rescale_numerical_columns(data=input_data)
     
    classes = get_classes(target_data=target_data)

    train_test_dict = split_data(input_=numerical_data, output_=target_data, test_data_ratio=TEST_DATA_RATIO)
    
    
# Run the main function
main()