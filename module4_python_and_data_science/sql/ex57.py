import pandas as pd

# Load the CSV file
input_file = "eurofxref-hist.csv"
output_file = "fixed.csv"

# Automatically ignore completely empty rows while reading the CSV file
df = pd.read_csv(input_file, skip_blank_lines=True)

# Drop columns where ALL elements are missing, that's N/A
df = df.dropna(axis=1, how="all")

# Save the DataFrame to a CSV file without writing the index column
df.to_csv(output_file, index=False)

print(f"Fixed CSV saved as: {output_file}")