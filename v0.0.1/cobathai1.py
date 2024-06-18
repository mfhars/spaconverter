import os
import pandas as pd
import datetime  # Import the datetime module

# Define the directory containing CSV files
folder_path = r"C:\Users\user\Documents\rigamarole\hasilmentah\ricko"  # Replace with your actual path

normalized_path = os.path.normpath(folder_path)  # Converts to "C:/Users/YourName/Desktop/Folder"

# Empty list to store DataFrames
all_dfs = []
all_headers = []  # Initialize the list to store headers

# Loop through all files in the folder
for filename in os.listdir(normalized_path):
    if filename.endswith(".csv"):
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

    

# Remove duplicate columns based on exact values
merged_df = merged_df.loc[:, ~merged_df.T.duplicated()]  # Transpose for column-wise comparison

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the output file name
output_filename = f"merged_data_{timestamp}.csv"  # You can change this name

# Specify the desired output directory
desired_folder_path = "C:/Users/user/Documents/rigamarole/hasilmentah"

# Save the merged DataFrame to a CSV file
merged_df.to_csv(os.path.join(desired_folder_path, output_filename), index=False)

print(f"Merged data saved to: {desired_folder_path}/{output_filename}")