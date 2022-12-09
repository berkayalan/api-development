import pandas as pd 

def prepare_data(path_to_data, encoding="latin-1"):
    """
        @params:
            - path_to_data: the path to the data
            - encoding: the encoding format to be used
        @return:
            - dictionary with following keys: 
                - text: the actual text message
                - label: the label associated to that text message
    """
    # Read data from path
    data = pd.read_csv(path_to_data)

    training_data = data.drop("Outcome",axis=1)
    target_data = data["Outcome"].values #We will predict Outcome(diabetes) 

    return training_data, target_data

def create_train_test_data(X, y, random_state):

    X_train = X.iloc[:600]
    X_test = X.iloc[600:]
    y_train = y[:600]
    y_test = y[600:]

    return {'x_train': X_train, 'x_test': X_test,
            'y_train': y_train, 'y_test': y_test}