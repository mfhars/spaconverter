import pandas as pd

# Sample data for three CSV files
data1 = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
data2 = {'col1': [4, 5, 6], 'col2': ['d', 'e', 'f']}
data3 = {'col1': [7, 8, 9], 'col2': ['g', 'h', 'i']}

# Create pandas DataFrames from the data
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Combine DataFrames horizontally
merged_df = pd.concat([df1, df2, df3], axis=1)

# Print the merged DataFrame
print(merged_df)
