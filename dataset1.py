import pandas as pd
import numpy as np

# Generate synthetic data (500 rows)
np.random.seed(42)
num_rows = 500

data = {
    'longitude': np.random.uniform(-124.3, -114.3, num_rows),
    'latitude': np.random.uniform(32.5, 42.5, num_rows),
    'housing_median_age': np.random.randint(1, 60, num_rows),
    'total_rooms': np.random.randint(500, 8000, num_rows),
    'total_bedrooms': np.random.randint(50, 1500, num_rows),
    'population': np.random.randint(100, 5000, num_rows),
    'households': np.random.randint(50, 2000, num_rows),
    'median_income': np.round(np.random.uniform(1.0, 10.0, num_rows), 1),
    'median_house_value': np.random.randint(50000, 500000, num_rows),
    'ocean_proximity': np.random.choice(
        ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'],
        size=num_rows,
        p=[0.2, 0.4, 0.2, 0.19, 0.01]
    )
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('housing_data.csv', index=False)
print("Dataset saved as 'synthetic_housing_data.csv'")
