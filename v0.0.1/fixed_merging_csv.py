import os
import pandas as pd

# Path to the folder containing the CSV files
folder_path = r"C:\Users\pingk\OneDrive - Chulalongkorn University\Documents\mekargit\zaytalnakhil-1\Kerjaan\fixed_import_to_be_merged_csv"

# Path to the folder where the merged CSV will be saved
export_folder_path = r"C:\Users\pingk\OneDrive - Chulalongkorn University\Documents\mekargit\zaytalnakhil-1\Kerjaan\fixed_export_merged_csv"

# Initialize variables
file_count = 0
row_count_before_merge = 0
all_dfs = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        # Increment file counter
        file_count += 1

        # Remove the ".CSV" extension from filename
        file_base = filename[:-4]  # Slicing to exclude the last 4 characters

        # Dynamically generate headers with "absorbance" and unique filename
        headers = [f"absorbance_{file_base}", file_base]

        # Read the CSV file into a DataFrame, specify capital CSV extension
        # Skip the first row (header row) of each CSV file
        df = pd.read_csv(os.path.join(folder_path, filename), skiprows=1, header=None, engine='python')  # May require adjustments based on CSV format

        # Increment row counter
        row_count_before_merge += len(df)

        # Append the DataFrame and its corresponding headers to separate lists
        all_dfs.append(df)

# Merge all DataFrames in the list
merged_df = pd.concat(all_dfs, ignore_index=True)

# Save the merged DataFrame to a CSV file in the specified export folder
output_filename = os.path.join(export_folder_path, 'merged_data.csv')
merged_df.to_csv(output_filename, index=False)