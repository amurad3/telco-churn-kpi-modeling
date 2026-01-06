import pandas as pd

input_path = "data/raw/Telco_customer_churn.xlsx"
output_path = "data/raw/telco_churn.csv"

df = pd.read_excel(input_path)
df.to_csv(output_path, index=False)

print("CSV created at:", output_path)
