import os
import spectrochempy as scp
import pandas as pd

# Define the input directory containing SPA files and the output directory for CSV files
input_dir = 'C:\\Users\\pingk\\Downloads\\coba\\sumber\\'  # Update this path
output_dir = 'C:\\Users\\pingk\\Downloads\\coba\\hasil\\'  # Update this path

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# List all SPA files in the input directory
spa_files = [f for f in os.listdir(input_dir) if f.endswith('.spa')]

# Function to sanitize the OMNIC name for use as a filename
def sanitize_filename(name):
    return "".join([c if c.isalnum() or c in "._-" else "_" for c in name])

for spa_file in spa_files:
    # Construct the full path to the SPA file
    spa_path = os.path.join(input_dir, spa_file)
    
    # Load the SPA file using Spectrochempy
    dataset = scp.read_omnic(spa_path)
    
    # Assuming the dataset contains a single spectrum, we extract the wavenumber and intensity
    wavenumbers = dataset.x.data.flatten()
    intensities = dataset.data.flatten()
    
    # Extract the internal OMNIC name
    omnic_name = dataset.name
    
    # Sanitize the OMNIC name to create a valid filename
    sanitized_name = sanitize_filename(omnic_name)
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame({'Wavenumber': wavenumbers, 'Intensity': intensities})
    
    # Construct the output CSV file path using the sanitized OMNIC name
    csv_file = os.path.join(output_dir, f'{sanitized_name}.csv')
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    
    print(f'Exported {spa_file} to {csv_file}')
