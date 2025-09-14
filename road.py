import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

# ----------------------
# 1️⃣ Load and prepare data
# ----------------------
df = pd.read_csv("road.csv", parse_dates=['Accident Date'], dayfirst=True)
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.hour

# ----------------------
# 2️⃣ Analysis & Visualizations
# ----------------------

# Accidents by Road Surface Conditions
plt.figure(figsize=(8,5))
sns.countplot(y='Road_Surface_Conditions', data=df, order=df['Road_Surface_Conditions'].value_counts().index)
plt.title("Accidents by Road Surface Conditions")
plt.tight_layout()
plt.show()

# Accidents by Junction Control
plt.figure(figsize=(8,5))
sns.countplot(y='Junction_Control', data=df, order=df['Junction_Control'].value_counts().index)
plt.title("Accidents by Junction Control")
plt.tight_layout()
plt.show()

# Accidents by Weather Conditions
plt.figure(figsize=(8,5))
sns.countplot(y='Weather_Conditions', data=df, order=df['Weather_Conditions'].value_counts().index)
plt.title("Accidents by Weather Conditions")
plt.tight_layout()
plt.show()

# Accidents by Time of Day
plt.figure(figsize=(10,5))
sns.histplot(df['Hour'], bins=24, kde=False)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

# ----------------------
# 3️⃣ Accident Hotspots Map
# ----------------------
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=13)
heat_data = df[['Latitude', 'Longitude']].dropna().values.tolist()
HeatMap(heat_data).add_to(m)
m.save("accident_hotspots.html")

print("Analysis complete! Charts displayed and heatmap saved as 'accident_hotspots.html'.")
