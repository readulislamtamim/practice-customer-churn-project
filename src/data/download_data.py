#%%
import os
import sys

PROJECT_NAME = 'practice-customer-churn-project'

try:

    from google.colab import drive
    drive.mount('/content/drive')
    
    PROJECT_ROOT = f'/content/drive/My Drive/Data Science/PnTDS/04_Projects/{PROJECT_NAME}'

    print("Running in Google Colab.")

except:

    PROJECT_ROOT = rf'G:/My Drive/Data Science/PnTDS/04_Projects/{PROJECT_NAME}'

    print("Running in local environment.")

# Move to project root
os.chdir(PROJECT_ROOT)

print("Current working directory:", os.getcwd())

# Add project root to Python path
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


#%%
import pandas as pd

#%%

url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

df = pd.read_csv(url)

raw_data_path = "data/raw/telco_churn_raw.csv"

df.to_csv(raw_data_path, index=False)

#%%
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print("\nColumns name:")

for column in df.columns:
    print(f"-   {column}")
