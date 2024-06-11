import pandas as pd

# Load the CSV file into a DataFrame
file_input = input(
    "Enter the name of the input file without the file ending: \n")
input_file = file_input+'.csv'
df = pd.read_csv(input_file)

# Select the desired columns
selected_columns = ['column1', 'column2', 'column3', 'column4']
new_df = df[selected_columns]

# Save the selected columns to a new CSV file
file_output = input(
    "Enter the name of the output file without the file ending: \n")
output_file = file_output+'.csv'
new_df.to_csv(output_file, index=False)

print(f"New CSV file created with selected columns: {selected_columns}")
