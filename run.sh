# Shell script to run the Medical Fraud Detection Tool

echo "Tool Initializing ..."

# Run code to join datasets - Inpatient Data, Outpatient Data and Beneficiary Data
python FraudDetection/preprocessing/data_join.py

# Run data preprocessing code 
python FraudDetection/preprocessing/preprocessing.py

# Run Main Function to initialize flask app
python FraudDetection/script/main.py

echo "Tool Ready"