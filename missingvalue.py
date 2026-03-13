import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, None, 30, None, 28],
    "Salary": [50000, 60000, None, 55000, None],
    "Department": ["HR", "IT", None, "Finance", "IT"]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())
print(df.isnull().sum())

df_dropped = df.dropna()
print(df_dropped)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["Department"].fillna("Unknown", inplace=True)

print(df)

df_forward = df.fillna(method="ffill")
print(df_forward)

df_backward = df.fillna(method="bfill")
print(df_backward)