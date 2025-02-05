import pandas as pd

# Load the Excel file
excel_file_path = "C:\Users\HP\Documents\Amazon Sale Report.csv"

# Read the Excel file
df = pd.read_excel(excel_file_path, engine='openpyxl')

# Define the CSV file path
csv_file_path = "C:\Users\HP\Documents\Custom Office Templates"

# Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Excel file has been successfully converted to CSV and saved at {csv_file_path}")
