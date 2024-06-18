import os
import pandas as pd

# Define the directory containing CSV files
folder_path = "C:/Users/user/Documents/Kerjaan/CSVs_All Samples/THAILAND/01_Nakhon Si Tammarat/2/Run21"  # Replace with your actual path

# Empty list to store DataFrames
all_dfs = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".CSV"):
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

    # Define the output file name
    output_filename = "merged_data.csv"  # You can change this name

    print(f"Number of columns in merged DataFrame: {len(merged_df.columns)}")

    # Specify the desired output directory
    desired_folder_path = "C:/Users/user/Documents/rigamarole/hasilmentah"

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv(os.path.join(desired_folder_path, output_filename), index=False)

    print(f"Merged data saved to: {desired_folder_path}/{output_filename}")
