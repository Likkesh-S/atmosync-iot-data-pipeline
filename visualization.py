import pandas as pd
import matplotlib.pyplot as plt

# Load telemetry data
df = pd.read_csv("../data/cleaned_telemetry_data.csv")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create temperature trend chart
plt.figure(figsize=(10, 5))
plt.plot(
    df["timestamp"],
    df["temperature_c"],
    marker="o",
    linewidth=2
)

plt.title("AtmoSync Temperature Trend")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig("../dashboard/temperature_trend.png", dpi=300)

# Display chart
plt.show()
