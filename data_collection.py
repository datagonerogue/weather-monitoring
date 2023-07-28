import argparse
import requests
from datetime import date
import pandas as pd
import time


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

def handle_weather(raw_data):
  temp = raw_data['main']['temp']
  weather = raw_data['weather'][0]['description']
  humidity = raw_data['main']['humidity']
  wind_speed = raw_data['wind']['speed']

  current_date = date.today().strftime('%Y-%m-%d')

  return current_date, temp, weather, humidity, wind_speed

def gen_df(current_date,temp, weather, humidity, wind_speed):
  info = {
    'Time': [current_date],
    'Temperature': [temp],
    'Weather': [weather],
    'Humidity': [humidity],
    'Wind Speed': [wind_speed]
  }
  dataframe = pd.DataFrame(info)
  return dataframe

args = parse_arguments()
api_key = args.api_key
city_name = args.city_name
days = args.days

for day in range(days):
    if day == 0:
        print("Initiating API Request")
    print(f"Fetching data for day {day + 1}")
    # Getting Raw Data of the API Response.
    raw_data=get_weather(api_key,city_name)
    # Filtering the Raw Data into list of Date and Data.
    current_date, temp, weather, humidity, wind_speed= handle_weather(raw_data)

    # Generating a DataFrame.
    dataframe = gen_df(current_date,temp, weather, humidity, wind_speed)
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
