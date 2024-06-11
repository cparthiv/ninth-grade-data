import pandas as pd

# Prompt the user for the input file name
input_file = input("Please enter the input CSV file name: ")

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Print each column name to the console
for column in df.columns:
    print(column)
