import pandas as pd
import sqlite3

''' Data 
customerID: Unique identifier for each customer.
gender: Gender of the customer (Male (0), Female (1)).
SeniorCitizen: Whether the customer is a senior citizen or not (1: Yes, 0: No).
Partner: Whether the customer has a partner or not (Yes (0), No (1)).
Dependents: Whether the customer has dependents or not (Yes, No).
tenure: Number of months the customer has stayed with the company.
PhoneService: Whether the customer has a phone service or not (Yes, No).
MultipleLines: Whether the customer has multiple lines or not (Yes, No, No phone service).
InternetService: Type of internet service the customer has (DSL, Fiber optic, No).
OnlineSecurity: Whether the customer has online security or not (Yes, No, No internet service).
OnlineBackup: Whether the customer has online backup or not (Yes, No, No internet service).
DeviceProtection: Whether the customer has device protection or not (Yes, No, No internet service).
TechSupport: Whether the customer has tech support or not (Yes, No, No internet service).
StreamingTV: Whether the customer has streaming TV or not (Yes, No, No internet service).
StreamingMovies: Whether the customer has streaming movies or not (Yes, No, No internet service).
Contract: The contract term of the customer (Month-to-month, One year, Two year).
PaperlessBilling: Whether the customer has paperless billing or not (Yes, No).
PaymentMethod: The payment method of the customer (Electronic check, Mailed check, Bank transfer, Credit card).
MonthlyCharges: The amount charged to the customer monthly.
TotalCharges: The total amount charged to the customer.
Churn: Whether the customer churned or not (Yes, No).
'''


# Load the CSV file
dataSet = pd.read_csv("Telco-Customer-Churn.csv")

# Droped the customerID no need as of now
dataSet.drop("customerID", axis=1, inplace=True)

#debugging 
print(dataSet.head(10))
print(dataSet.shape)
print(dataSet.columns)

#debugging Area
print(dataSet.head(10))

connet = sqlite3.connect("telecom_dbase.db")

dataSet.to_sql("customer_Info",connet, if_exists="replace",index=False)
#debugging Area 
debugPrint = pd.read_sql_query("SELECT * FROM customer_Info;", connet)
print(debugPrint)


#Removing row that has Null value in any of the columns 
connet.execute(""" DELETE FROM customer_Info WHERE 
        gender IS NULL OR
        SeniorCitizen IS NULL OR
        Partner IS NULL OR
        Dependents IS NULL OR
        tenure IS NULL OR
        PhoneService IS NULL OR
        MultipleLines IS NULL OR
        InternetService IS NULL OR
        OnlineSecurity IS NULL OR
        OnlineBackup IS NULL OR
        DeviceProtection IS NULL OR
        TechSupport IS NULL OR
        StreamingTV IS NULL OR
        StreamingMovies IS NULL OR
        Contract IS NULL OR
        PaperlessBilling IS NULL OR
        PaymentMethod IS NULL OR
        MonthlyCharges IS NULL OR
        TotalCharges IS NULL OR
        Churn IS NULL;
""")

# data Encoding
''' Encoding Info: in binary 
    1. Gender: Male: 0 and Female: 1
    2. Partner, Dependents, PhoneService, Paper less, churn: yes (1) or no(0) 
'''
dataFrame = pd.read_sql_query("SELECT * FROM customer_Info", connet)

column_Encoding = ['gender', 'Partner', 'Dependents','PhoneService','PaperlessBilling','Churn']

for column in column_Encoding:
    dataFrame[column] = dataFrame[column].map({'Yes':1, 'No':0, 'Male':0, 'Female':1})
dataFrame.to_sql("customer_Info",connet, if_exists="replace",index=False)

#debugging Area
print("\n")
debugPrint = pd.read_sql_query("SELECT * FROM customer_Info;", connet)
print(debugPrint)
