import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

print("\nFIRST 5 RECORDS:\n")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nDATASET INFORMATION:")
print(df.info())

print("\nNULL VALUES:")
print(df.isnull().sum())

# Remove missing values
df.dropna(inplace=True)

# Rename columns if necessary
df.columns = df.columns.str.strip()

print("\nCLEANED DATASET")
print(df.head())

# ==========================
# STATE WISE UNEMPLOYMENT
# ==========================

plt.figure(figsize=(14,6))

sns.barplot(
    data=df,
    x='Region',
    y='Estimated Unemployment Rate (%)'
)

plt.xticks(rotation=90)

plt.title("State Wise Unemployment Rate")

plt.show()

# ==========================
# AREA WISE COMPARISON
# ==========================

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x='Area'
)

plt.title("Urban vs Rural Records")

plt.show()

# ==========================
# CORRELATION HEATMAP
# ==========================

numeric_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# ==========================
# HISTOGRAM
# ==========================

plt.figure(figsize=(8,5))

plt.hist(
    df['Estimated Unemployment Rate (%)'],
    bins=20
)

plt.title("Distribution of Unemployment Rate")

plt.xlabel("Unemployment Rate")

plt.ylabel("Frequency")

plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY")