import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Step 2: Convert 'hour_beginning' to datetime
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# Step 3: Define a function to categorize time of day
def categorize_time(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Step 4: Extract hour from timestamp and apply time-of-day categorization
df['hour'] = df['hour_beginning'].dt.hour
df['time_of_day'] = df['hour'].apply(categorize_time)

# Step 5: Group by time of day and calculate average pedestrian counts
time_of_day_stats = df.groupby('time_of_day')['Pedestrians'].mean()

# Reorder categories for proper plotting
ordered_stats = time_of_day_stats.reindex(['Morning', 'Afternoon', 'Evening', 'Night'])

# Step 6: Plot average pedestrian count by time of day
plt.figure(figsize=(8, 5))
ordered_stats.plot(kind='bar')
plt.title("Average Pedestrian Counts by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Average Pedestrian Count")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
