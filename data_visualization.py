import pandas as pd
import matplotlib.pyplot as plt
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Weather Forecast Visualization Script")
    parser.add_argument("CSV_File", type=str, help="Path to CSV file for the data requiired")
    return parser.parse_args()
    
args = parse_arguments()
csv = args.CSV_File

data = pd.read_csv(csv)
data['Time'] = pd.to_datetime(data['Time'])  # Convert the 'Time' column to datetime format

plt.figure(figsize=(14, 12))  # Set the figure size (width, height)
plt.plot(data['Time'], data['Temperature'], marker='.', linestyle='-', color='red')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation')
plt.xticks(rotation=45)
plt.savefig('temperature_plot.png')
