import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/home/belladonna/Devlopment/Project-Weather_Forecast_Visualization/weather_info(2023-07-21).csv')
plt.plot(data['Time'], data['Temperature'])
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot')
plt.grid(True)
plt.savefig('line_plot.png')