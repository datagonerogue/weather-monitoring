import requests
from datetime import date
import pandas as pd
import time


def get_weather(api_key,city_name): 
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
  response = requests.get(url)  
  raw_data = response.json()
  return raw_data

def handle_temp(raw_data,date_list,data_list):
  temperature = raw_data['main']['temp']
  current_date = date.today().strftime('%Y-%m-%d')
  date_list.append(current_date)
  data_list.append(temperature)  
  return current_date,date_list, data_list

def data_type(date_list,data_list):
    while True:
        data_type= input("Enter the Type of Forcast Data (temprature): ")
        if data_type=='temprature' :
            return handle_temp(raw_data,date_list,data_list)
        else: 
          print('Data not Available, Enter the Data correctly.')

def gen_df(date_list,temp_list):
  info={
    'Time' :date_list,
    'Temperature':temp_list
  }
  dataframe = pd.DataFrame(info)
  return dataframe



if __name__ == "__main__":

  while True:
    date_list=[]
    data_list=[]
    current_date=''
    # Taking Input of the API and the City.
    api_key, city_name = input("Enter the API key and the name of the city (seperated by a space): ").split()

    # Getting Raw Data of the API Response.
    raw_data=get_weather(api_key,city_name)

    # Filtering the Raw Data into list of Date and Data.
    current_date,date_list, data_list= data_type(date_list,data_list)

    # Generating a DataFrame.
    dataframe=gen_df(date_list,data_list)

    # Generating a CSV File
    dataframe.to_csv(f'weather_info{current_date}.csv', index=False)

    print(f"The data is in the created file: 'weather_info{current_date}.csv'")
    break #time.sleep(24 * 60 * 60)

    