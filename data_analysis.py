import pandas as pd

# Load cleaned telemetry data
df = pd.read_csv("../data/cleaned_telemetry_data.csv")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create hourly time column
df["telemetry_hour"] = df["timestamp"].dt.floor("h")

# Calculate hourly environmental metrics
hourly_metrics = df.groupby("telemetry_hour").agg(
    ping_count=("device_id", "count"),
    avg_temp_c=("temperature_c", "mean"),
    peak_temp_c=("temperature_c", "max"),
    min_temp_c=("temperature_c", "min"),
    avg_humidity_pct=("humidity_pct", "mean"),
    avg_pressure_hpa=("pressure_hpa", "mean")
).reset_index()

# Round numeric values
numeric_columns = [
    "avg_temp_c",
    "peak_temp_c",
    "min_temp_c",
    "avg_humidity_pct",
    "avg_pressure_hpa"
]
hourly_metrics[numeric_columns] = hourly_metrics[numeric_columns].round(2)

# Save hourly metrics
hourly_metrics.to_csv("../data/hourly_metrics.csv", index=False)

print("Hourly analysis completed successfully.")
print("\nHourly Metrics:")
print(hourly_metrics)
