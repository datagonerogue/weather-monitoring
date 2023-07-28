import requests
from datetime import date
import pandas as pd
import time


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



if __name__ == "__main__":

  while True:
    temp_list = []
    weather_list = []
    humidity_list = []
    wind_speed_list = []
    current_date = ''

    # Taking Input of the API and the City.
    days = int(input("Enter the number of days you want to collect daily data for: "))
    api_key, city_name = input("Enter the API key and the name of the city (seperated by a space): ").split()
    print("Getting the Initial Response...")

    for _ in range(days):
        # Getting Raw Data of the API Response.
        raw_data=get_weather(api_key,city_name)

        # Filtering the Raw Data into list of Date and Data.
        current_date, temp_list, weather_list, humidity_list, wind_speed_list= handle_weather(raw_data, temp_list, weather_list, humidity_list, wind_speed_list)

        # Generating a DataFrame.
        dataframe = gen_df(current_date,temp_list, weather_list, humidity_list, wind_speed_list)
        desired_columns = ['Time', 'Temperature', 'Weather', 'Humidity', 'Wind Speed']

        # Generating a CSV File
        dataframe.to_csv(f'weather_info{current_date}.csv', index=False)
        print(f'''
        --------------------------------------------------------
        {dataframe}
        --------------------------------------------------------
        ''')

        dataframe.to_csv(f'weather_info_{city_name}_{current_date}.csv', index=False)
        time.sleep(24 * 60 * 60)    