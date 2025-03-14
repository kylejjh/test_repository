'''
Part 2 - Pandas

1. From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

2. Replace missing values in Min.Price and Max.Price columns with their respective mean.

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

3. How to get the rows of a dataframe with row sum > 100?

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
'''

import pandas as pd
import numpy as np

# Attempt to load the dataset from the URL
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'

try:
    df = pd.read_csv(url)
    print("Dataset loaded successfully from URL.")
except Exception as e:
    print("️Failed to load dataset from URL. Using mock data instead.")

    # Create mock dataset in case of failure
    data = {
        "Manufacturer": ["Ford", "Toyota", "Honda", "BMW", "Audi"] * 4,
        "Model": ["Focus", "Camry", "Civic", "X5", "A4"] * 4,
        "Type": ["Sedan", "Sedan", "Sedan", "SUV", "Sedan"] * 4,
        "Min.Price": [10, np.nan, 15, np.nan, 22] * 4,
        "Max.Price": [20, 25, np.nan, 40, np.nan] * 4
    }
    df = pd.DataFrame(data)

# 1. Select every 20th row starting from row 0
filtered_df = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print("\n Filtered Manufacturer, Model, Type:")
print(filtered_df)

# 2. Replace NaN values in 'Min.Price' and 'Max.Price' with their respective mean
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
print("\n Updated DataFrame with Imputed Prices:")
print(df[['Manufacturer', 'Min.Price', 'Max.Price']].head())

# 3. Create a random DataFrame and filter rows where the sum > 100
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
filtered_rows = df_random[df_random.sum(axis=1) > 100]
print("\n Rows with Sum > 100:")
print(filtered_rows)
