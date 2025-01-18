import pandas as pd

# Load the dataset
file_path = "/download/wps-data.csv"
df = pd.reading_csv(file_path)

# Display the first few rows to understand the structure
df.head()

# Display column names to identify relevant variables
df.columns.tolist()[:50]  # Show only the first 50 column names for readability
