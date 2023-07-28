import argparse
import requests
from datetime import date
import pandas as pd
import time
from jinja2 import Environment, FileSystemLoader

def parse_arguments():
    parser = argparse.ArgumentParser(description="Weather Forecast Visualization Script")
    parser.add_argument("api_key", type=str, help="API key for the weather data")
    parser.add_argument("city_name", type=str, help="Name of the city for weather forecast")
    parser.add_argument("days", type=int, default=7, help="Number of days for weather forecast (default: 7)")
    return parser.parse_args()

def get_weather(api_key,city_name): 
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}'
  response = requests.get(url)  
  raw_data = response.json()
  return raw_data

def handle_weather(raw_data, temp_list, weather_list, humidity_list, wind_speed_list):
  temperature = raw_data['main']['temp']
  weather_desc = raw_data['weather'][0]['description']
  humidity = raw_data['main']['humidity']
  wind_speed = raw_data['wind']['speed']

  temp_list.append(temperature)
  weather_list.append(weather_desc)
  humidity_list.append(humidity)
  wind_speed_list.append(wind_speed)
  
  current_date = date.today().strftime('%Y-%m-%d')

  return current_date, temp_list, weather_list, humidity_list, wind_speed_list

def gen_df(current_date,temp_list, weather_list, humidity_list, wind_speed_list):
  info = {
    'Time': current_date,
    'Temperature': temp_list,
    'Weather': weather_list,
    'Humidity': humidity_list,
    'Wind Speed': wind_speed_list
  }
  dataframe = pd.DataFrame(info)
  return dataframe

temp_list = []
weather_list = []
humidity_list = []
wind_speed_list = []
current_date = ''
args = parse_arguments()
api_key = args.api_key
city_name = args.city_name
days = args.days
# Create the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('dataframe_template.html')
for day in range(days):
    if day == 0:
        print("Initiating API Request")
    print(f"Fetching data for day {day + 1}")
    # Getting Raw Data of the API Response.
    raw_data=get_weather(api_key,city_name)
    # Filtering the Raw Data into list of Date and Data.
    current_date, temp_list, weather_list, humidity_list, wind_speed_list= handle_weather(raw_data, temp_list, weather_list, humidity_list, wind_speed_list)
    # Generating a DataFrame.
    dataframe = gen_df(current_date,temp_list, weather_list, humidity_list, wind_speed_list)
    # Reindex the DataFrame with the desired columns order
    desired_columns = ['Time', 'Temperature', 'Weather', 'Humidity', 'Wind Speed']
    dataframe = dataframe.reindex(columns=desired_columns)
    # Format the DataFrame to HTML using Jinja2
    dataframe_html = dataframe.to_html(classes='data', escape=False, index=False)
    # Render the template with the DataFrame HTML
    output_html = template.render(dataframe=dataframe_html)
    # Save the styled DataFrame to an HTML file
    output_file_path = f'weather_info_{city_name}.html'
    with open(output_file_path, 'a') as f:
        f.write(output_html)
    print(f"The data is saved in the file: {output_file_path}")
    # Save the styled DataFrame to an CSV file
    dataframe.to_csv(f'weather_info_{city_name}.csv', index=False, mode='a', header=not day)
    print(f"The data is also saved in the CSV file: 'weather_info_{city_name}_{current_date}.csv'")
    print(f"Data for day {day + 1} is saved.")
    if day < days - 1:
        print('''
        -------------------------
        Waiting for 24 hours
        -------------------------
        ''')
        time.sleep(24 * 60 * 60)

print("All data is saved.")
