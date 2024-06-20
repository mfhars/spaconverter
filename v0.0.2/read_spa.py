from LoadSpectrum import read_spa
import pathlib
import csv
import os

basepath = 'C:\\Users\\pingk\\Downloads\\coba\\sumber\\'
output_path = 'C:\\Users\\pingk\\Downloads\\coba\\hasil\\New Folder\\'
paths = [str(x) for x in list(pathlib.Path(basepath).rglob('*.spa'))]
print('Files detected: {}'.format(len(paths)))

# Create output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

for path in paths:
    spectra_tmp, wavelength_tmp, title_tmp = read_spa(path)
    print(spectra_tmp, wavelength_tmp, title_tmp)

    # Assuming spectra_tmp and wavelength_tmp are lists of the same length
    # Replace ':' with '_'
    title_tmp = title_tmp.replace(':', '_')

    # Check if file already exists, if so, append a number to make it unique
    counter = 1
    original_title = title_tmp
    while os.path.isfile(f'{output_path}{title_tmp}.csv'):
        title_tmp = f"{original_title}_{counter}"
        counter += 1

    with open(f'{output_path}{title_tmp}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Spectra', 'Wavelength'])  # Writing headers
        writer.writerows(zip(spectra_tmp, wavelength_tmp))  # Writing data