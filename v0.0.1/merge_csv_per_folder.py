import os
import pandas as pd

# Define the directory containing CSV files
folder_path = "C:\Users\user\Documents\rigamarole\hasilmentah\ricko"  # Replace with your actual path

# Empty list to store DataFrames
all_dfs = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".CSV"):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(folder_path, filename))
        # Append the DataFrame to the list
        all_dfs.append(df)
    else:
        print(f"Skipping non-CSV file: {filename}")

# Check if any files were found
if not all_dfs:
    print("No CSV files found in the specified folder.")
else:
    # Combine DataFrames horizontally if files were found
    merged_df = pd.concat(all_dfs, axis=1)
    print(merged_df)
