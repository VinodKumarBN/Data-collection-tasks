import pandas as pd

data = {
    'Name': ['Riya', 'Karan', None, 'Meena', 'Amit', None, 'Sneha', 'Vikas', 'Neha', 'Tina'],
    'Age': [28, 30, 22, None, 26, 21, None, 24, 29, None],
    'Gender': ['F', 'M', 'M', 'F', 'M', 'M', 'F', 'M', 'F', 'F'],
    'Score': [91, None, 76, 84, 89, 95, None, 88, 93, 90]
}

df = pd.DataFrame(data)
df.to_csv('raw_data.csv', index=False)
print("Data saved to 'raw_data.csv'.")

df_read = pd.read_csv('raw_data.csv')
print("\n First 5 rows of the dataset:")
print(df_read.head())

df_dropped = df_read.dropna()
print("\nData after dropping rows with missing values:")
print(df_dropped)

print("\nMissing values in each column:")
print(df_read.isnull().sum())

df_filled = df_read.copy()
df_filled['Name'].fillna('some name', inplace=True)
df_filled['Age'].fillna(21, inplace=True)

print("\n Data after filling missing values:")
print(df_filled)

df_filled.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_data.csv'.")
