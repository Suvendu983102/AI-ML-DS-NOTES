import pandas as pd

# Creating DataFrame
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
}
df = pd.DataFrame(data)

# Basic operations
print(df.head())      # First 5 rows
print(df.info())      # Information about data
print(df.describe())  # Statistical summary

# Data cleaning
df.dropna()          # Remove missing values
df.fillna(0)         # Fill missing with 0
df["Age"] = df["Age"].astype(int)  # Convert type