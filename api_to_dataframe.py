import requests
from datetime import date
import pandas as pd
import time


def get_weather(api_key='65326f47edebc6d805c9ecf9238d1f7f',city_name='Delhi'): 

  url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
  response = requests.get(url)  
  data = response.json()
  return data

def handle_temp(raw_data,date_list,temp_list):

  temperature = raw_data['main']['temp']
  current_date = date.today().strftime('%Y-%m-%d')
  date_list.append(current_date)
  temp_list.append(temperature)  

  return current_date, temperature , date_list, temp_list

def gen_df(date_list,temp_list):
  info={
    'Time' :date_list,
    'Temperature':temp_list
  }
  dataframe = pd.DataFrame(info)
  return dataframe

if __name__ == "__main__":
  date_list = []
  temp_list = []

  while True:
    raw_data=get_weather()
    current_date, temperature,date_list,temp_list = handle_temp(raw_data,date_list,temp_list)
    dataframe=gen_df(date_list,temp_list)
    dataframe.to_csv(f'/home/belladonna/Devlopment/Project-Weather_Forecast_Visualization/weather_info({current_date}).csv', index=False)
    
    break #time.sleep(24 * 60 * 60)

    