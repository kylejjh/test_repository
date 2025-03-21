import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Step 2: Convert 'hour_beginning' to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# Step 3: Extract the day of the week (0 = Monday, ..., 6 = Sunday)
df['day_of_week'] = df['hour_beginning'].dt.dayofweek

# Step 4: Map day numbers to actual weekday names
day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
           4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
df['day_name'] = df['day_of_week'].map(day_map)

# Step 5: Filter for weekdays (Monday to Friday -> day_of_week < 5)
weekdays_df = df[df['day_of_week'] < 5]

# Step 6: Group by weekday name and calculate total pedestrian counts
weekday_counts = weekdays_df.groupby('day_name')['Pedestrians'].sum()

# Step 7: Reorder the days for correct plotting order
weekday_counts = weekday_counts.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

# Step 8: Plot the data
plt.figure(figsize=(10, 5))
plt.plot(weekday_counts.index, weekday_counts.values, marker='o')
plt.title("Total Pedestrian Counts by Weekday")
plt.xlabel("Day of the Week")
plt.ylabel("Total Pedestrian Count")
plt.grid(True)
plt.tight_layout()
plt.show()
