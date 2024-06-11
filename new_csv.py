import pandas as pd

# Load the CSV file into a DataFrame
file_input = input(
    "Enter the name of the input file without the file ending: \n")
input_file = file_input+'.csv'
df = pd.read_csv(input_file)

# Select the desired columns
selected_columns = []
while True:
    column = input("Enter the name of a column (or 'stop' to finish): ")
    if column == 'stop':
        break
    if column not in df.columns:
        print("Invalid column name. Please try again.")
        continue
    selected_columns.append(column)

new_df = df[selected_columns]

# Save the selected columns to a new CSV file
file_output = input(
    "Enter the name of the output file without the file ending: \n")
output_file = file_output+'.csv'
new_df.to_csv(output_file, index=False)

print(f"New CSV file created with selected columns: {selected_columns}")
