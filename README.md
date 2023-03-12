# Fraud-Detection

[![build_test](https://github.com/sagnikgh1899/FraudDetection/actions/workflows/build_test.yml/badge.svg)](https://github.com/sagnikgh1899/FraudDetection/actions/workflows/build_test.yml)
[![Coverage Status](https://coveralls.io/repos/github/sagnikgh1899/FraudDetection/badge.svg?branch=main)](https://coveralls.io/github/sagnikgh1899/FraudDetection?branch=main)


#### PROJECT TYPE
Analysis and Research Tool

#### TEAM MEMBERS
Sagnik Ghosal, Ishank Vasania, Prerit Chaudhary, Neel Shah

#### QUESTIONS OF INTEREST
1. Can we predict which are fraudulent claims out of all claims from a given medical claims data quickly and accurately?
2. Which providers are doing the most fraud? Are there any specific years or specific states where the number of fraud claims were high?
3. Are there specific patterns in frauds specific to providers and medical insurance claims? 
4. What are the trends of claims across beneficiary demographics?

#### PROJECT GOAL
The goal of the project is to build an infrastructure that can be used to identify fraudulent providers and gain insights into specific facilities, providers, and physicians who may be engaging in fraudulent activity. The Infrastructure will consists of 2 main parts: Visualization (comprising various different insights), Modelling (comprising ML models that will identify fradulent claims)

#### DATA SOURCES
-----------------
We have used the following 4 different datasets for the various analysis and model development: [Inpatient Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Inpatientdata-1542865627584.csv), [Outpatient Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Outpatientdata-1542865627584.csv), [Beneficiary Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Beneficiarydata-1542865627584.csv), and [Fraud Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train-1542865627584.csv). 

#### ORGANIZATION OF THE PROJECT
--------------------------------
The project has the following structure:

    FraudDetection/
      |- .github/workflows/
         |- build_test.yml
      |- FraudDetection/
         |- models/
            |- __init__.py
            |- models.py
         |- performance/
            |- __init__.py
            |- performance.py
         |- script/
            |- json/
                |- models_performance.json
            |- uploads/
                |- README.md
            |- __init__.py
            |- main.py
         |- static/
            |- images/
                |- Amount_Reimbursed.jpg
                |- DiagnosisGroupCode.jpg
                |- days_admitted_visualization.jpg
                |- download.jpg
                |- map.jpg
                |- visualization1.jpg
                |- visualization2.jpg
                |- visualization3.jpg
                |- visualization4.jpg
            |- download_fraudulent_csv.js
            |- sort_table_rows_based_on_metrics.js
         |- templates/
            |- start-page.htm
            |- user-page.htm
         |- tests/
            |- __init__.py
            |- test_FraudDetection.py
         |- .coveragerc
      |- data/
         |- .DS_Store
         |- State_Mapping.csv
         |- Train-1542865627584.csv
         |- Train_Beneficiarydata-1542865627584.csv
         |- Train_Inpatientdata-1542865627584.csv
         |- Train_Outpatientdata-1542865627584.csv
         |- merged.csv
      |- doc/
         |- Component Specification.md
         |- Functional Specification.md
         |- Interaction_Diagram_Use_Case_1.jpg
         |- Interaction_Diagram_Use_Case_2.jpg
         |- Interaction_Diagram_Use_Case_3.jpg
         |- Technology_Review_Medical_Provider_Fraud.pptx
      |- preprocessing/
         |- README.md
         |- data_join.py
         |- initial_eda.py
         |- preprocessing.py
      |- .gitignore
      |- .pylintrc
      |- LICENSE
      |- README.md
      |- environment.yml
      |- requirements.txt
      |- setup.py


#### INSTALLATION
-----------------
Start by cloning FraudDetection on your own computer by using the following git command:

```
git clone https://github.com/sagnikgh1899/FraudDetection.git
```

Next, to install the package you will need to go into the FraudDetection directory and run the setup.py file:
 
```
cd FraudDetection/
python setup.py install
```
    
To ensure that the dependencies to run FraudDetection are installed on your computer you will want to run the following command:

```
pip install -r requirements.txt
```

#### EXAMPLES
-------------
To understand how to use FraudDetection, please refer to 
the [examples](https://github.com/sagnikgh1899/FraudDetection/tree/main/FraudDetection/examples) section of this GitHub page where you can find 
examples for doing the following:
- Creating visualizations by merging the 4 datasets
- Creating visualizations from the input test dataset
- Generating a csv file of potentially fraudulent claims from the input test dataset
- Adding or removing fraud detection models


#### LIMITATIONS AND FUTURE SCOPE
---------------------------------
** Improve prediction performance by including SOTA DL models
** Gather and use data from more states
** Present the visualization analysis city-wise

#### ACKNOWLEDGEMENTS
---------------------
A thanks to DATA 515 course professor, Melissa Winstanley and the teaching assistants, of the University of Washington, for instructing and guiding us on the best practices of software design and development.

#### CONTACT
------------
Questions? Comments? Drop us a line at fraud.detect@gmail.com
