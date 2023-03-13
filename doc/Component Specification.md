#### Software Components
* **Data Preprocessing Component**
    * ***What it does***: This component preprocesses raw data from four sources: Inpatient Data, Outpatient Data, Beneficiary Data, and Fraud Data. It cleans, normalizes, and formats the data to make it compatible with the machine learning models used for vizualization and prediction purposes.
    * ***Input***: Raw data from four sources, namely, Inpatient Data, Outpatient Data, Beneficiary Data, and Fraud Data.
    * ***Output***: Clean and formatted dataset ready for analysis.
* **Claims Metadata Analysis Visualization Component**
    * ***What it does***: This component visualizes patient demographics in insurance claims, such as state-wise percentage fraudulent claims, and factors like days admitted, diagnosis group code, and insurance claim reimbursement. It helps users pinpoint areas of high risk for fraud and focus their investigations.
    * ***Input***: Pre-processed data containing patient demographics, claim type, and other relevant metadata.
    * ***Output***: Visualizations such as bar charts and map representations, showing metrics related to patient demographics, diagnosis group code, and reimbursement amounts for the pre-processed dataset.
* **Fraud Detection Component**
    * ***What it does***: This component uses machine learning algorithms such as clustering, regression, and ensemble to identify potential fraud claims in a test dataset. By doing so, it highlights only the suspicious claims for further investigation, saving the user time and effort. This component also decides the best performing model based on the model's performance on the pre-processed dataset. 
    * ***Input***: A test dataset having patient demographics, claim type, and other relevant metadata.
    * ***Output***: A list of flagged claims.
* **Fraud Detection Results Visualization Component**
    * ***What it does***: MENTION THIS
    * ***Input***: A test dataset having patient demographics, claim type, and other relevant metadata.
    * ***Output***: Visualizations such as bar charts and map representations, showing metrics related to .... for the test dataset.


#### Interactions to Accomplish Use Cases
- ***Use Case 1: Visualizing Fraud Patterns in Medicare Claims Data*** -- The Data Preprocessing Component is responsible for taking in raw data from four different sources and processing it to prepare it for analysis. Once the data is preprocessed, it is passed onto the Claims Metadata Analysis Visualization Component, which generates visualizations to provide valuable insights into various aspects such as patient demographics, claim type, disbursement amount, and more. These visualizations are interactive and allow the user to explore and investigate the data, aiding in their decision-making process.
![Interaction Diagram - Use Case 1](Interaction_Diagram_Use_Case_1.jpg)
- ***Use Case 2: Identifying Potentially Fraudulent Claims for Review in a New Dataset*** -- The Fraud Detection Component performs fraud detection on a new test dataset provided by the user. It uses the best fraud detection model to label each claim in the test dataset with a 0 or 1, where 0 indicates a non-fraudulent claim and 1 indicates a fraudulent claim. The claims that are labeled as 1 are then written to a CSV file, which can be downloaded by the user by clicking on the download button. This allows the user to focus on potentially fraudulent claims instead of having to manually investigate all of the claims.
![Interaction Diagram - Use Case 3](Interaction_Diagram_Use_Case_3.jpg)
- ***Use Case 3: Analyzing Medicare Claims with Visualizations for a New Dataset*** -- The Fraud Detection Component is responsible for analyzing a new test dataset provided by the user. It utilizes the best fraud detection model to label each claim in the test dataset with either 0 (non-fraudulent) or 1 (fraudulent) based on its assessment. The labelled data is then passed on to the Fraud Detection Results Visualization Component, which generates visualizations to offer insights into various aspects such as patient demographics, claim type, disbursement amount, and more. These visualizations can be interacted with by the user to guide their investigations and decision-making process.
![Interaction Diagram - Use Case 3](Interaction_Diagram_Use_Case_3.jpg)

#### Preliminary Plan
- **Week 8**:
    * Finalize dataset for the analysis and fraud detection.
    * Decide which anomaly detection models to use and test them on the available dataset.
    * Prepare dashboard for the analysis of the prediction results for the different anomaly detection models.
    * Identify interesting patterns and prepare visualization to illustrate them.
- **Week 9**:
    * Complete preparing the dashboard which hosts both the models and the visualizations.
    * Create python package folder and test files.
    * Create Examples folder that contains examples of using the packages.
- **Week 10**:
    * Polish code to be PEP8 compliant and add appropriate documentation on how to use the tools.
    * Create README file that gives an overview of the project, LICENSE file and setup file that initializes the project after it has been cloned.
    * Create final project presentation.
    * Prepare demo for the final presentation.
- **Week 11**:
    * Final presentation and demo of the project on 14th March.
