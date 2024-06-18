import os
import pandas as pd
import datetime  # Import the datetime module

# Define the directory containing CSV files
folder_path = "C:/Users/user/Documents/rigamarole/hasilmentah/ricko"  # Replace with your actual path

# Empty list to store DataFrames
all_dfs = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(folder_path, filename))
        # Append the DataFrame to the list
        all_dfs.append(df)

# Check if any files were found
if not all_dfs:
    print("No CSV files found in the specified folder.")
else:
    # Combine DataFrames horizontally if files were found
    merged_df = pd.concat(all_dfs, axis=1)
    
    print(f"Number of columns in merged DataFrame: {len(merged_df.columns)}")

    

# Remove duplicate columns based on exact values
merged_df = merged_df.loc[:, ~merged_df.T.duplicated()]  # Transpose for column-wise comparison


timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the output file name
output_filename = f"merged_data__{timestamp}.csv"  # You can change this name


# Specify the desired output directory
desired_folder_path = "C:/Users/user/Documents/rigamarole/hasilmentah"

# Save the merged DataFrame to a CSV file
merged_df.to_csv(os.path.join(desired_folder_path, output_filename), index=False)

print(f"Merged data saved to: {desired_folder_path}/{output_filename}")
