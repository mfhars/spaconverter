import os
import pandas as pd
import datetime

# Define the directory containing CSV files
folder_path = "C:\\Users\\pingk\\OneDrive - Chulalongkorn University\\RandomDatas\\folder sementara\\BATCH20240423_ForConversion_01"  # Replace with your actual path

# Empty list to store DataFrames
all_dfs = []
all_headers = []  # Initialize the list to store headers

# Initialize counters
file_count = 0
row_count_before_merge = 0

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
        all_headers.extend(headers)  # Add headers to the list

# Check if any files were found
if not all_dfs:
    print("No CSV files found in the specified folder.")
else:
    # Combine DataFrames horizontally if files were found
    merged_df = pd.concat(all_dfs, axis=1)

    # Set the column headers for the merged DataFrame using the all_headers list
    merged_df.columns = all_headers

    # Print number of columns before selection
    print("Number of columns before selection:")
    print(merged_df.shape[1])

# Select every other column starting from the 2nd column (0-indexed)
merged_df = merged_df.iloc[:, ::2]

# Create a boolean mask for duplicated columns
dup_mask = merged_df.columns.duplicated(keep='first')

# Select only the non-duplicated columns
merged_df = merged_df.loc[:, ~dup_mask]

# Print number of columns after selection
print("Number of columns after selection:")
print(merged_df.shape[1])

print(f"Number of files read: {file_count}")
print(f"Number of rows before merge: {row_count_before_merge}")

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the output file name
output_filename = f"merged_data_{timestamp}.csv"  # You can change this name

# Specify the desired output directory
desired_folder_path = "C:\\Users\\pingk\\OneDrive - Chulalongkorn University\\RandomDatas\\folder sementara\\CSV_Individual_Batches\\BATCH20240423_ForConversion_01_CSV"  # Replace with your actual target path

# Check if the directory exists, if not, create it
if not os.path.exists(desired_folder_path):
    os.makedirs(desired_folder_path)

# Save the merged DataFrame to a CSV file
merged_df.to_csv(os.path.join(desired_folder_path, output_filename), index=False)

print(f"Merged data saved to: {desired_folder_path}/{output_filename}")