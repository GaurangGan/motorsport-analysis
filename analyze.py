import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
data = {
    'Driver': ['Lewis Hamilton', 'Max Verstappen', 'Valtteri Bottas', 'Charles Leclerc'],
    'Race1_LapTimes': [90, 91, 92, 93],
    'Race2_LapTimes': [88, 87, 89, 90],
}

df = pd.DataFrame(data)

# Data Analysis
df['Average_LapTime'] = df[['Race1_LapTimes', 'Race2_LapTimes']].mean(axis=1)

# Data Visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for average lap times
ax.bar(df['Driver'], df['Average_LapTime'], color='skyblue')
ax.set_ylabel('Average Lap Time')
ax.set_title('Average Lap Time Comparison')

# Show the plot
plt.show()
