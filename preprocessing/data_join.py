"""
Module to merge the data into a single dataframe.
Dataset to join: fraud, beneficiary, inpatient, outpatient
to generate,please run function generate_merged_file(),
it will automatically generate the merged file in data folder.
imports: numpy, pandas
"""
# import numpy as np
import pandas as pd


def read_data():
    """
    function to read csv files
    parameters: None
    return: data frames fraud, beneficiary, inpatient, outpatient.
    raise FileExistsError: raises an exception when file is not found
    """
    try:
        fraud=pd.read_csv("data/Train-1542865627584.csv")
        beneficiary=pd.read_csv("data/Train_Beneficiarydata-1542865627584.csv")
        inpatient=pd.read_csv("data/Train_Inpatientdata-1542865627584.csv")
        outpatient=pd.read_csv("data/Train_Outpatientdata-1542865627584.csv")
        return fraud, beneficiary, inpatient, outpatient
    except FileExistsError as error:
        raise error


def join_inpatient_outpatient(inpatient, outpatient):
    """
    function to merge inpatient, outpatient dataframe
    parameters: inpatient, outpatient
    return: merged dataframe
    """
    inpatient_outpatient=pd.merge(outpatient,inpatient,
        left_on=['BeneID', 'ClaimID', 'ClaimStartDt', 'ClaimEndDt', 'Provider',
        'InscClaimAmtReimbursed', 'AttendingPhysician', 'OperatingPhysician',
        'OtherPhysician', 'ClmDiagnosisCode_1', 'ClmDiagnosisCode_2',
        'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5',
        'ClmDiagnosisCode_6', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8',
        'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10', 'ClmProcedureCode_1',
        'ClmProcedureCode_2', 'ClmProcedureCode_3', 'ClmProcedureCode_4',
        'ClmProcedureCode_5', 'ClmProcedureCode_6', 'DeductibleAmtPaid',
        'ClmAdmitDiagnosisCode'],
        right_on=['BeneID', 'ClaimID', 'ClaimStartDt', 'ClaimEndDt', 'Provider',
        'InscClaimAmtReimbursed', 'AttendingPhysician', 'OperatingPhysician',
        'OtherPhysician', 'ClmDiagnosisCode_1', 'ClmDiagnosisCode_2',
        'ClmDiagnosisCode_3', 'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5',
        'ClmDiagnosisCode_6', 'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8',
        'ClmDiagnosisCode_9', 'ClmDiagnosisCode_10', 'ClmProcedureCode_1',
        'ClmProcedureCode_2', 'ClmProcedureCode_3', 'ClmProcedureCode_4',
        'ClmProcedureCode_5', 'ClmProcedureCode_6', 'DeductibleAmtPaid',
        'ClmAdmitDiagnosisCode']
                                ,how='outer')
    return inpatient_outpatient


def join_inpatient_outpatient_beneficiary(inpatient_outpatient, beneficiary):
    """
    function to merge merged df, beneficiary dataframe
    parameters: inpatient, outpatient merged and beneficiary
    return: merged dataframe
    """
    inpatient_outpatient_beneficiary=pd.merge(inpatient_outpatient,beneficiary,
                                left_on='BeneID',right_on='BeneID',how='inner')
    return inpatient_outpatient_beneficiary


def join_inpatient_outpatient_beneficiary_fraud(inpatient_outpatient_beneficiary, fraud):
    """
    function to merge merged df, fraud dataframe
    parameters: inpatient, outpatient merged, beneficiary and fraud
    return: merged dataframe
    """
    inpatient_outpatient_beneficiary_fraud=pd.merge(fraud,inpatient_outpatient_beneficiary,
                                                    on='Provider')
    return inpatient_outpatient_beneficiary_fraud


def join_csv(fraud, beneficiary, inpatient, outpatient):
    """
    function to join csv files. Joining by key BeneID, Provider.
    parameters: fraud, beneficiary, inpatient, outpatient dataframes
    return: merged csv
    """
    # Join the files
    merged = join_inpatient_outpatient(inpatient, outpatient)
    merged = join_inpatient_outpatient_beneficiary(merged, beneficiary)
    merged = join_inpatient_outpatient_beneficiary_fraud(merged, fraud)

    # Save the merged file as a CSV
    merged.to_csv('data/merged.csv', index=False)


def generate_merged_data():
    """
    m ainfunction to join csv files. calls read_data and join_csv functions
    parameters: None
    return: None
    """
    fraud, beneficiary, inpatient, outpatient = read_data()
    join_csv(fraud, beneficiary, inpatient, outpatient)


def main():
    """
    main function
    parameters: None
    return: None
    """
    generate_merged_data()


if __name__ == "__main__":
    main()
