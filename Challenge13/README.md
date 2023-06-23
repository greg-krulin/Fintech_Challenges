# Venture Funding with Deep Learning

This project aims to predict the success of startups receiving venture funding using a neural network model. It is specifically designed to assist Alphabet Soup, a venture capital firm, in making funding decisions. The model has been trained on a CSV file containing data from over 34,000 organizations that have received funding from Alphabet Soup in the past.

## Prerequisites

Before running the project, ensure that the following libraries are installed:

- Pandas
- TensorFlow
- Scikit-learn

## Data

The input data file is `applicants_data.csv`. It contains comprehensive information about businesses that have received funding from Alphabet Soup, including whether they ultimately became successful.

The data was preprocessed by performing the following steps:

- Reading the dataset from a CSV file into a Pandas DataFrame.
- Dropping the 'EIN' (Employer Identification Number) and 'NAME' columns from the DataFrame as they are not relevant to the model.
- Encoding categorical variables using OneHotEncoder and creating a new DataFrame with these encoded variables.
- Concatenating the DataFrame with encoded variables and the original DataFrame's numerical variables.
- Creating the features (X) and target (y) datasets. The target dataset is defined by the preprocessed DataFrame column "IS_SUCCESSFUL", with the remaining columns defining the features dataset.
- Splitting the features and target sets into training and testing datasets with random_state=1.
- Scaling the features data using the StandardScaler from scikit-learn.

## Model Architecture and Training

Three models were developed with different architectures, all using 'relu' as the activation function for the hidden layers and 'linear' for the output layer. All models were compiled using 'binary_crossentropy' as the loss function, 'adam' as the optimizer, and 'accuracy' as the metrics.

- The original model: This model has an input layer of 116 features, two hidden layers with 8 neurons for the first layer and 5 neurons for the second layer, and one unit for the output layer.
- Alternative Model 1: This model has the same number of input features, one hidden layer with an average of the input and output (58 neurons), and one unit for the output layer.
- Alternative Model 2: This model, like the others, has the same number of input features, but it has one hidden layer with 2/3 of the input plus the output (78 neurons), and one unit for the output layer.

## Model Results

### Original Model

- Loss: 0.5973
- Accuracy: 72.68%

The original model outperformed the others with the lowest loss value and high accuracy. It successfully predicts startup success with an accuracy of 72.68% and a loss of 0.5973.

### Alternative Model 1

- Loss: 0.6229
- Accuracy: 72.64%

The first alternative model's performance slightly trailed the original, with a marginally higher loss value but nearly the same accuracy.

### Alternative Model 2

- Loss: 0.7317
- Accuracy: 72.68%

Despite achieving the same accuracy as the original model, the second alternative model suffered from a higher loss value. This indicates that while the model's accuracy is on par with the best-performing model, its predictive ability may not be as reliable due to the higher loss value.
