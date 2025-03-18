import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load climate change dataset (Assuming CSV file with 'Year', 'Temperature', 'CO2', 'Sea_Level')
data = pd.read_csv("climate_data.csv")

# Convert Year to datetime
data["Year"] = pd.to_datetime(data["Year"], format='%Y')

# Plot temperature anomaly over time
plt.figure(figsize=(12, 6))
plt.plot(data["Year"], data["Temperature"], marker='o', linestyle='-', color='red')
plt.title("Global Temperature Anomaly Over Time")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid()
plt.show()

# CO2 emissions vs. Temperature scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data["CO2"], y=data["Temperature"], hue=data["Year"].dt.year, palette="coolwarm")
plt.title("CO2 Emissions vs Temperature Anomaly")
plt.xlabel("CO2 Concentration (ppm)")
plt.ylabel("Temperature Anomaly (°C)")
plt.colorbar()
plt.show()

# Sea Level Rise over the years
fig = px.line(data, x="Year", y="Sea_Level", title="Sea Level Rise Over Time")
fig.update_xaxes(title_text="Year")
fig.update_yaxes(title_text="Sea Level Rise (mm)")
fig.show()

# Heatmap of correlation between climate variables
plt.figure(figsize=(8, 6))
sns.heatmap(data[["Temperature", "CO2", "Sea_Level"]].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Between Climate Variables")
plt.show()

# Display summary statistics
print(data.describe())
