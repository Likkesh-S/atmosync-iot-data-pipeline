import pandas as pd

# Load telemetry dataset
df = pd.read_csv("../data/telemetry_data.csv")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Remove duplicate records
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Sort records by device and timestamp
df = df.sort_values(["device_id", "timestamp"])

# Save cleaned dataset
df.to_csv("../data/cleaned_telemetry_data.csv", index=False)

print("Data cleaning completed successfully.")
print("Number of cleaned records:", len(df))
print("\nCleaned data:")
print(df)
