import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/customer_churn.csv")

# 1️⃣ Overall Churn Rate
churn_rate = (df['churn'].value_counts(normalize=True) * 100).round(2)
print("Churn Rate (%):")
print(churn_rate)

# -------------------------------------------------------

# 2️⃣ Churn by Contract Type
contract_churn = pd.crosstab(df['contract_type'], df['churn'], normalize='index') * 100
print("\nChurn Rate by Contract Type (%):")
print(contract_churn.round(2))

# -------------------------------------------------------

# 3️⃣ Revenue Loss Due to Churn
revenue_loss = df[df['churn'] == 'Yes']['monthly_charges'].sum()
print("\nEstimated Monthly Revenue Loss:", revenue_loss)

# -------------------------------------------------------

# 4️⃣ Tenure Group Analysis
df['tenure_group'] = pd.cut(
    df['tenure'],
    bins=[0, 12, 24, 100],
    labels=['0-12 Months', '12-24 Months', '24+ Months']
)

tenure_churn = pd.crosstab(df['tenure_group'], df['churn'])
print("\nChurn by Tenure Group:")
print(tenure_churn)

# -------------------------------------------------------

# 5️⃣ Top High-Risk Customers
high_risk = df[df['churn'] == 'Yes'].sort_values(
    by='monthly_charges',
    ascending=False
).head(10)

print("\nTop 10 High-Risk Customers:")
print(high_risk[['customer_id', 'monthly_charges', 'tenure']])

# -------------------------------------------------------

# 6️⃣ Visualization - Churn Distribution
df['churn'].value_counts().plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
