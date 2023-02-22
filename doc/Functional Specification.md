#### Background
Provider fraud is a major issue in the Medicare system. The government has reported that the amount of money spent on Medicare has increased significantly due to fraudulent claims. This type of fraud involves providers, physicians, and beneficiaries working together to submit false claims for medical services. Through careful analysis of Medicare data, it has been discovered that many physicians engage in fraudulent practices. These practices involve using ambiguous diagnosis codes to charge for costly procedures and drugs. Insurance companies are heavily impacted by these bad practices, leading to increased insurance premiums and making healthcare more expensive for everyone. Healthcare fraud takes many forms, but some of the most common types include billing for services that were never provided, submitting duplicate claims, misrepresenting services provided, charging for more complex or expensive services than were actually provided, and billing for a covered service when the service provided was not covered.

#### Problem Statement
The goal of the project is to build a system that the government can use to identify fraudulent providers and gain insights into specific facilities, providers, and physicians who may be engaging in fraudulent activity.

#### User Profile
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
We are using 4 different datasets for this project which can be accessed [here](https://www.kaggle.com/code/rohitrox/medical-provider-fraud-detection/data): 
- **Beneficiary Data** - Present in the form of a CSV file. Has 138556 rows and 25 attributes. Some of the attributes include Beneficiary id, DOB, gender, country, information on existing medical conditions among others.
- **Inpatient Data** - Inpatient data refers to the medical data of patients who have been admitted to a hospital or other healthcare facility for an overnight stay or longer. The data is present in the form of a CSV file. Has 40474 rows and 30 attributes. Some of the attributes include Beneficiary id, Provider id, Claim start date, attending physician among others.
- **Outpatient Data** - Outpatient data refers to the medical data of patients who receive medical care or treatment at a healthcare facility without being admitted for an overnight stay. The data is present in the form of a CSV file. Has 517737 rows and 27 attributes. Some of the attributes include Beneficiary id, Provider id, Claim start date, attending physician among others.
- **Fraud (Yes/No) Data** - Present in the form of a CSV file. Has 5410 rows and 2 attributes, which are Provider id, Fraud yes or no.

##### Use Cases
- **Use Case 1**: Identifying High-Risk Claims for Review
    * ***Objective***: The purpose of this use case is to identify claims that are likely to be fraudulent and flag them for further review and investigation.
    * ***Expected Interactions***: The process begins when a patient submits their claim data to the provider portal/claim form. The government medicare agency receives the claim and checks it for authenticity. The agency can then use our API, where our machine-learning model is hosted, to check the probability of a fraudulent claim. The model analyzes the data and generates a fraud score or probability for each claim. Based on the score, the government medicare agency can prioritize claims with the highest fraud scores for further investigation. This can potentially lead to the prevention of fraudulent payments, which saves time and money for both the government and patients.
- **Use Case 2**: Prioritizing Claims for Payment Processing
    * ***Objective***: This use case aims to prioritize claims for payment processing based on their likelihood of being fraudulent. This helps to reduce the risk of making fraudulent payments.
    * ***Expected Interactions***: Patients will input their claim data into the provider portal or claim form, which will be submitted to the government Medicare agency for review. The government agency can then use our API, where our machine-learning model is hosted, to check the probability of a fraudulent claim. The model will analyze the data for each claim and generate a fraud score or likelihood. Based on this score, the user can prioritize claims with low fraud scores for payment processing, which will help to lower the risk of fraudulent payments and save taxpayer money.
- **Use Case 3**: Analyzing Medicare Claims through Visualization
    * ***Objective***: The purpose of this use case is to investigate Medicare claims data by visualizing it and identifying trends, patterns, and anomalies that could indicate fraudulent activities.
    * ***Expected Interactions***: The government user would access a dashboard or a web-based interface that displays various visualization tools, such as charts, graphs, and maps, showing data related to Medicare claims. The user would interact with the visualization tools, selecting different data points, filters, and parameters to view the data from different angles. The user could also drill down into specific areas of interest and thoroughly examine the data to detect trends and patterns that could suggest fraudulent activity. Moreover, the visualization tools could be used to compare different data sets, such as claims from various providers or regions, to detect disparities or anomalies that require further investigation. Finally, the visualizations could be downloaded or exported for additional analysis and reporting. In summary, this use case aims to provide the government with a user-friendly and interactive way to visually explore and analyze Medicare claims data, facilitating the identification of potential fraud and abuse more effectively.





