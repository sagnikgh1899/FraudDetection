#### Background
---------------
Provider fraud is a major issue in the Medicare system. The government has reported that the amount of money spent on Medicare has increased significantly due to fraudulent claims. This type of fraud involves providers, physicians, and beneficiaries working together to submit false claims for medical services. Through careful analysis of Medicare data, it has been discovered that many physicians engage in fraudulent practices. These practices involve using ambiguous diagnosis codes to charge for costly procedures and drugs. Insurance companies are heavily impacted by these bad practices, leading to increased insurance premiums and making healthcare more expensive for everyone. Healthcare fraud takes many forms, but some of the most common types include billing for services that were never provided, submitting duplicate claims, misrepresenting services provided, charging for more complex or expensive services than were actually provided, and billing for a covered service when the service provided was not covered.

#### Problem Statement
----------------------
The goal of the project is to build a system that the government can use to identify fraudulent providers and gain insights into specific facilities, providers, and physicians who may be engaging in fraudulent activity.

#### User Profile
-----------------
- ***Government Medicare Agency***:
The Government Medicare Agency is responsible for verifying and approving legitimate claims and rejecting fraudulent ones. To prevent fraudulent claims from being paid, the agency takes targeted actions.
    * Have access to claims data and want to use it to determine whether a claim is fraudulent or not. By using a model that assigns a higher likelihood of fraud to certain claims, the agency can focus on reviewing those claims while letting go of the non-flagged ones, which can save a lot of time and money.
    * They are not familiar with the Python programming language.
    * Can analyze the claims data and identify patterns, providers, or physicians involved in fraudulent activity.
- ***Developer***:
The developer is a person who is responsible for maintaining and ensuring that the fraud detection model works properly. The developer is skilled and knowledgeable about the technical aspects of the model.
    * Updates the fraud detection model frequently whenever new features are available to ensure it's up to date.
    * Updates the visualization of the model based on new requirements or feedback from stakeholders.

#### Data Sources
-----------------
We are using 4 different datasets for this project which can be accessed [here](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data): 
- **[Beneficiary Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Beneficiarydata-1542865627584.csv)** - Present in the form of a CSV file. Has 138556 rows and 25 attributes. Some of the attributes include Beneficiary id, DOB, gender, country, information on existing medical conditions among others.
- **[Inpatient Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Inpatientdata-1542865627584.csv)** - Inpatient data refers to the medical data of patients who have been admitted to a hospital or other healthcare facility for an overnight stay or longer. The data is present in the form of a CSV file. Has 40474 rows and 30 attributes. Some of the attributes include Beneficiary id, Provider id, Claim start date, attending physician among others.
- **[Outpatient Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train_Outpatientdata-1542865627584.csv)** - Outpatient data refers to the medical data of patients who receive medical care or treatment at a healthcare facility without being admitted for an overnight stay. The data is present in the form of a CSV file. Has 517737 rows and 27 attributes. Some of the attributes include Beneficiary id, Provider id, Claim start date, attending physician among others.
- **[Fraud Data](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data?select=Train-1542865627584.csv)** - Present in the form of a CSV file. Has 5410 rows and 2 attributes, which are Provider id, Fraud yes or no.

##### Use Cases
---------------
- **Use Case 1**: Visualizing Fraud Patterns in Medicare Claims Data
    * ***Objective***: The objective of this use case is to create informative and intuitive visualizations that can effectively showcase the patterns and trends of fraudulent activities within Medicare claims data. The goal is to help identify potential fraudulent cases and make data-driven decisions to prevent and reduce fraud.
    * ***Expected Interactions***: As a government Medicare agency, the user will be interested in visualizing the fraud patterns in Medicare claims data. To achieve this, the user interacts with a visual dashboard that will display various fraud metrics and insights in a user-friendly way. The dashboard will have different charts such as bar charts, pie charts, map representations to display different metrics. These visualizations are interactive and allow the user to explore and investigate the data, aiding in their decision-making process.
- **Use Case 2**: Identifying Potentially Fraudulent Claims for Review in a New Dataset
    * ***Objective***: The objective for this use case is to develop a fraud detection system that can analyze a new dataset of medical claims and identify potentially fraudulent claims for review. The system should use machine learning algorithms to identify patterns and anomalies in the data and generate a list of flagged claims.
    * ***Expected Interactions***: As a government Medicare agency, the user's primary objective is to identify potentially fraudulent claims for review in a new dataset. To achieve this, the user would first need to upload the new dataset containing medical claims data to the system. Once the detection process is complete, the system would generate a list of potentially fraudulent claims. The user would then review these flagged claims and instigate appropriate investigations.
- **Use Case 3**: Analyzing Medicare Claims with Visualizations for a New Dataset
    * ***Objective***: The objective of this use case is to analyze a new dataset of Medicare claims using visualizations such as bar charts, pie-charts, and funnel charts. The analysis will focus on metrics related to the percentage of fraud and non-fraud, as well as the number of fraudulent cases in inpatient and outpatient cases. The goal is to gain insights into the data and identify potential instances of fraud.
    * ***Expected Interactions***: As a government Medicare agency, the user is interested in analyzing a new dataset of Medicare claims to gain insights into potential fraudulent activities. To do this, the user can access the fraud detection tool, which utilizes various machine learning algorithms to detect potential fraudulent activities. The user can input the new dataset into the tool and run the analysis. After the analysis is completed, the tool generates various visualizations, including bar charts, pie charts, and funnel charts, to help the user visualize key metrics related to the percentage of fraud and non-fraud, the number of fraudulent cases in inpatient and outpatient cases, and other relevant metrics. The user can interact with these visualizations to drill down into the data and gain deeper insights.
