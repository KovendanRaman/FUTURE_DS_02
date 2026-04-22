import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df.dropna(subset=['TotalCharges'], inplace=True)

def group_tenure(tenure):
    if tenure <= 12: return '0-1 Year'
    elif tenure <= 24: return '1-2 Years'
    elif tenure <= 36: return '2-3 Years'
    elif tenure <= 48: return '3-4 Years'
    elif tenure <= 60: return '4-5 Years'
    else: return '5+ Years'

df['Tenure_Group'] = df['tenure'].apply(group_tenure)

df.to_csv('cleaned_telco_churn.csv', index=False)
print("Clean Telco data exported successfully!")