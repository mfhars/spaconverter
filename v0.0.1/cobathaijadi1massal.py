import os
import pandas as pd

# Define the directory containing CSV files
folder_path = "C:/Users/user/Documents/Kerjaan/Thailand_Jadi_Satu"  # Replace with your actual path

# Empty list to store DataFrames
all_dfs = []
all_headers = []  # Initialize the list to store headers

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".CSV"):
        # Remove the ".CSV" extension from filename
        file_base = filename[:-4]  # Slicing to exclude the last 4 characters

        # Dynamically generate headers with "absorbance" and unique filename
        headers = [f"absorbance_{file_base}", file_base]

        # Read the CSV file into a DataFrame, specify capital CSV extension
        df = pd.read_csv(os.path.join(folder_path, filename), engine='python', encoding='latin-1')  # May require adjustments based on CSV format

        # Append the DataFrame and its corresponding headers to separate lists
        all_dfs.append(df)
        all_headers.extend(headers)  # Add headers to the list

# Check if any files were found
if not all_dfs:
    print("No CSV files found in the specified folder.")
else:
    # Combine DataFrames horizontally if files were found
    merged_df = pd.concat(all_dfs, axis=1)

    # Set the column headers for the merged DataFrame using the all_headers list
    merged_df.columns = all_headers

    

print(merged_df)