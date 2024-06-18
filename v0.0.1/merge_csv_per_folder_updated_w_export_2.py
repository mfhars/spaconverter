import os
import pandas as pd

# Define the directory containing CSV files
folder_path = "C:/Users/user/Documents/Kerjaan/CSVs_All Samples/THAILAND/01_Nakhon Si Tammarat/2/Run21"  # Replace with your actual path

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
        df = pd.read_csv(os.path.join(folder_path, filename), engine='python')  # May require adjustments based on CSV format

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

    # Define the output file name
    output_filename = "merged_data.csv"  # You can change this name

    # Specify the desired output directory
    desired_folder_path = "C:/Users/user/Documents/rigamarole/hasilmentah"

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv(os.path.join(desired_folder_path, output_filename), index=False)

    print(f"Merged data saved to: {desired_folder_path}/{output_filename}")

