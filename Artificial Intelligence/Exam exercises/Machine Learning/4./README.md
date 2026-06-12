A dataset on air pollution is provided, containing eight continuous features: temperature, humidity, wind speed, CO2 concentration, NO2 concentration, SO2 concentration, PM2.5 concentration, and PM10 concentration. You should derive the class attribute based on the PM10 concentration: if the value is greater than 50, the instance is labeled as high, otherwise as low.

Split the dataset into training and testing sets, using the first 70% of the data for training and the remaining 30% for testing.

You are required to evaluate how different preprocessing techniques affect the performance of a neural network with the following configuration: 50 neurons, ReLU activation, learning rate of 0.001, and 25 training epochs. For this purpose, the following preprocessing techniques should be applied:

Anomaly removal: for the attributes representing the concentrations of CO2, NO2, and SO2, all values exceeding their respective thresholds (C, N, and S) should be replaced with the corresponding threshold value.
Feature scaling: Apply standardization to all attributes.
Calculate the accuracy using (1) the original dataset, (2) removing anomalies, (3) standardizing all features, and (4) both removing anomalies and standardizing features.

The input thresholds C, N, and S should be read from standard input, in that order.

Print the classification accuracy of the neural network for each of the four preprocessing scenarios to standard output.

To ensure reproducibility and match the test cases, set random_state=0 when initializing the classifiers.

For ConvergenceWarnings

import warnings

warnings.filterwarnings("ignore")