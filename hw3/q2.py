import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Step 2: Convert the 'hour_beginning' column to datetime
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# Step 3: Filter the dataset for Brooklyn Bridge and year 2019
df_2019 = df[(df['location'] == 'Brooklyn Bridge') &
             (df['hour_beginning'].dt.year == 2019)]

# Step 4: Drop rows with missing values in 'weather_summary' or 'Pedestrians'
df_2019_clean = df_2019.dropna(subset=['weather_summary', 'Pedestrians'])

# Step 5: One-hot encode the 'weather_summary' column
weather_encoded = pd.get_dummies(df_2019_clean['weather_summary'])

# Step 6: Combine encoded weather columns with 'Pedestrians' column
encoded_df = pd.concat([df_2019_clean[['Pedestrians']], weather_encoded], axis=1)

# Step 7: Compute the correlation matrix
correlation_matrix = encoded_df.corr()

# Step 8: Plot a heatmap to show correlation between weather and pedestrian counts
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix[['Pedestrians']], annot=True, cmap="coolwarm")
plt.title("Correlation between Weather and Pedestrian Counts (Brooklyn Bridge, 2019)")
plt.show()
