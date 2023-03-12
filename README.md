# Fraud-Detection

[![build_test](https://github.com/sagnikgh1899/FraudDetection/actions/workflows/build_test.yml/badge.svg)](https://github.com/sagnikgh1899/FraudDetection/actions/workflows/build_test.yml)
[![Coverage Status](https://coveralls.io/repos/github/sagnikgh1899/FraudDetection/badge.svg?branch=main)](https://coveralls.io/github/sagnikgh1899/FraudDetection?branch=main)


#### PROJECT TYPE:
Analysis and Research Tool

#### TEAM MEMBERS:
Sagnik Ghosal, Ishank Vasania, Prerit Chaudhary, Neel Shah

#### QUESTIONS OF INTEREST:
1. Can we predict which are fraudulent claims out of all claims from a given medical claims data quickly and accurately?
2. Which providers are doing the most fraud? Are there any specific years or specific states where the number of fraud claims were high?
3. Are there specific patterns in frauds specific to providers and medical insurance claims? 
4. What are the trends of claims across beneficiary demographics?

#### PROJECT GOAL:
The goal of the project is to build an infrastructure that can be used to identify fraudulent providers and gain insights into specific facilities, providers, and physicians who may be engaging in fraudulent activity. The Infrastructure will consists of 2 main parts: Visualization (comprising various different insights), Modelling (comprising ML models that will identify fradulent claims)

#### DATA SOURCES:
We have used the following 4 different datasets for the various analysis and model development: [Inpatient Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Inpatientdata-1542865627584.csv), [Outpatient Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Outpatientdata-1542865627584.csv), [Beneficiary Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Beneficiarydata-1542865627584.csv), and [Fraud Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train-1542865627584.csv). 

#### ORGANIZATION OF THE PROJECT:
The project has the following structure:

    DATA515-Project/
      |- data/
         |- Taxi_samples/
            |- dimensions.txt
            |- taxi_04_2014_sample.csv
            |- taxi_05_2014_sample.csv
            |- taxi_06_2014_sample.csv
         |- Uber_samples/
            |- uber_04_2014_sample.csv
            |- uber_05_2014_sample.csv
            |- uber_06_2014_sample.csv
     	   |- NYC_Shapes.json
     	   |- NYC_Shapes_Cleaned.json     	 
      |- doc/
         |- Design_Specification_and_Project_Plan.pdf
         |- Functional_Specification.pdf
         |- Presentation_How_is_Uber_Changing_Taxi_in_New_York_City.pdf
         |- Technical_Review
      |- examples/
         |- EXAMPLES.md
      |- uberTaxi/
         |- script/
            |- check_points.py
            |- find_neighborhood.py
            |- geo_convert.py
            |- main.py
            |- process_coordinates.py
            |- queries.py
            |- random_sample.py
            |- read_json.py
            |- split_data.py
         |- test/
            |- TestAllFunction.py
      |- LICENSE
      |- README.md
      |- setup.py
      |- NYC_Uber_Taxi.html


#### INSTALLATION:
Describe installation -- see the AXWX example

#### EXAMPLES:
Describe examples -- see the AXWX example

#### LIMITATIONS:
Describe limitations -- see the AXWX example

#### ACKNOWLEDGEMENTS
A thanks to DATA 515 course professor, Melissa Winstanley and the teaching assistants, of the University of Washington, for instructing and guiding us on the best practices of software design and development.

#### CONTACT
Questions? Comments? Drop us a line at fraud.detect@gmail.com
