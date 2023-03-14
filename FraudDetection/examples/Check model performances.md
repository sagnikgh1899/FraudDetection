### Check Model Performances on the Preprocessed Dataset
----------------------------------------------------------
We utilized five machine learning (ML) models, namely LODA, ECOD, COPOD, and IFOREST, from the PYOD library to perform our analysis. Further information on these models can be found on the [PYOD](https://pyod.readthedocs.io/en/latest/index.html) website. After preprocessing the dataset, we ran the models and the results are displayed on the Prediction page of our web application. Although it is not recommended to display model performance to users who may not be familiar with the models, we decided to include them for the purpose of this project. To reproduce the performance metrics, follow these steps:

First, ensure that you are in the root directory by running the command on the terminal:
```
cd FraudDetection/
```
The path should look something as follows:

![Initial path](example_model_performances2.jpg)

Before proceeding further, it's crucial to confirm that the "preprocessed.csv" file has been successfully generated and stored in the [data](https://github.com/sagnikgh1899/FraudDetection/tree/main/FraudDetection/data) folder. In case the file is missing, there is a need to execute certain commands on the terminal to generate the CSV file. Please refer to the following commands that can be run on the terminal to generate the file:
```
python FraudDetection/preprocessing/data_join.py
python FraudDetection/preprocessing/preprocessing.py
```
After generating the "preprocessed.csv" file, the next step is to evaluate the performance of the machine learning models used for fraud detection in the analysis. To accomplish this, run the following command:
```
python FraudDetection/performance/performance.py
```
Kindly note that the execution of this command will require some time (maximum of 8 minutes) to compute the performance metrics of the fraud detection models. The output will be similar to the following format:

![Output of model performances](example_model_performances1.jpg)

The output values are automatically written to the [models_performance.json](https://github.com/sagnikgh1899/FraudDetection/blob/main/FraudDetection/script/json/models_performance.json) file. While there may be slight variations between the listed values and the ones entered, the differences should be negligible.

----------------------
#### Challenges faced

Initially, the team had planned to implement various machine learning and deep learning models, including LOF, ABOD, KNN, VAE, and MO_GAAL, to improve fraud detection in the dataset. However, the execution time for these models was exceeding 60 minutes, and they were resulting in memory errors, making them computationally heavy for the team's computers. As a result, the team decided to exclude these models from the project.

------------------
#### Future Scope
Some potential enhancements that may be included in future releases are:
* Improved performance by integrating powerful yet computationally lightweight fraud detection models, thereby increasing the efficiency and accuracy of fraud detection.
