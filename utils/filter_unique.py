import pandas as pd

input_file = input("Please enter the input CSV file name: ")
df = pd.read_csv(input_file)

numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
multiple_choice_columns = [col for col in df.columns if df[col].nunique() < 10]

selected_columns = list(set(numerical_columns + multiple_choice_columns))
new_df = df[selected_columns]

output_file = input("Please enter the output CSV file name: ")
new_df.to_csv(output_file, index=False)

print(f"New CSV file created with selected columns: {selected_columns}")
