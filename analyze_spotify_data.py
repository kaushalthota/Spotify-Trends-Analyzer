
# Spotify Listening Trends Analyzer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("spotify_sample_data.csv")

# Parse date and extract useful time features
df['listen_date'] = pd.to_datetime(df['listen_date'])
df['month'] = df['listen_date'].dt.to_period('M')
df['hour'] = df['listen_date'].dt.hour

# Most played artists
top_artists = df['artist'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_artists.values, y=top_artists.index, palette="magma")
plt.title("Top 10 Most Played Artists")
plt.xlabel("Play Count")
plt.ylabel("Artist")
plt.tight_layout()
plt.savefig("top_artists.png")
plt.close()

# Listening habits by hour of day
hourly_counts = df['hour'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker="o")
plt.title("Listening Activity by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Listens")
plt.grid(True)
plt.tight_layout()
plt.savefig("listening_by_hour.png")
plt.close()

# Monthly streaming trend
monthly_counts = df['month'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_counts.index.astype(str), y=monthly_counts.values, palette="coolwarm")
plt.title("Monthly Listening Trend")
plt.xlabel("Month")
plt.ylabel("Total Plays")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_trend.png")
plt.close()

# Save summary report
summary = {
    "Most Played Artist": top_artists.idxmax(),
    "Top Genre": df['genre'].value_counts().idxmax(),
    "Busiest Listening Hour": hourly_counts.idxmax(),
    "Most Active Month": monthly_counts.idxmax().strftime('%B %Y')
}

with open("spotify_insights.txt", "w") as f:
    for key, value in summary.items():
        f.write(f"{key}: {value}\n")

print("Analysis complete. Visuals and summary report saved.")
