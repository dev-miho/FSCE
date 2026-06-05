We are given a dataset of fish characteristics. All attributes it contains are of continuous type. Your task is to train a classifier — a collection of decision trees — that will predict fish type classes using the first 85% of the given dataset. You need to calculate the accuracy obtained on the remaining 15% of the dataset. The part of the dataset where the column col_index has been removed is used.

In the starter code you are given the dataset. The input receives the index of the column to be removed (col_index). Additionally, the number of decision trees to be used is read, along with a value for the criterion for selecting the best attribute. Finally, a new record is read that needs to be classified using the trained classifier.

The output should print the accuracy of the classifier, the predicted class for the new record, and the probabilities of belonging to each class.

Note: since the values are of continuous type, there is no need to convert them to integer values.

To get the same results as in the test examples, set random_state=0 when creating the classifier.
