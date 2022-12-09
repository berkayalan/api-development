from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

def run_model_training(X_train, X_test, y_train, y_test):
    random_forest = RandomForestClassifier().fit(X_train,y_train)
    random_forest.score(X_test,y_test)
    y_pred = random_forest.predict(X_test)
    print(classification_report(y_test, y_pred))

    return random_forest