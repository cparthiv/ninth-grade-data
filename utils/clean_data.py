import pandas as pd

# Read the CSV file
df = pd.read_csv('multichoice.csv')

# Remove columns with uninterpretable data
# Replace 'column1' and 'column2' with the actual column names
# df = df.drop(columns=['column1', 'column2'])

# Replace strings within columns with numbers
for column in df.columns:
    unique_values = df[column].unique()
    if len(unique_values) > 10:
        df = df.drop(columns=[column])
    else:
        mapping = {value: i for i, value in enumerate(unique_values)}
        df[column] = df[column].map(mapping)

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_multichoice.csv', index=False)
