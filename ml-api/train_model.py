# Packages
import joblib

# Get customized functions from library
import packages.data_processor as dp
import packages.model_trainer as mt


# 0.Path to data
path_to_data = './data/diabetes.csv'

# 1.Prepare the data
training_data, target_data = dp.prepare_data(path_to_data)

# 2.Create train - test split
train_test_data = dp.create_train_test_data(training_data, target_data,2022)

# 3.Run training
model = mt.run_model_training(train_test_data['x_train'], train_test_data['x_test'], 
                           train_test_data['y_train'], train_test_data['y_test'])

# 4.Save the trained model and vectorizer
joblib.dump(model, './models/diabetes_detector_model.pkl')