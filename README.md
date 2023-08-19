# Weather Data Monitoring and Graphing

This Python project is designed to collect weather data for the current day, wait for 24 hours, collect data again, and repeat the process. The collected data is then stored in a .csv file for further analysis. Additionally, the project includes a script to visualize the data in a graph using a popular python library, matplotlib.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Data Visualization](#data-visualization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Weather Data Monitoring and Graphing is a Python project aimed at collecting weather data at regular intervals, storing it in a .csv file, and visualizing the data in graphical format using matplotlib. The data is collected for the current day and updated every 24 hours to monitor weather trends over time.

## Features

- Automated weather data collection at regular intervals (24 hours).
- Data storage in a .csv file for easy analysis.
- Visualization of weather data in a graphical format using matplotlib.

## Requirements

Before running the project, make sure you have the required dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```
You also need a Open Weather [API Key](https://openweathermap.org/api).
## Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/CTM_Giorno/weather-monitoring.git
```

2. Change into the project directory.

```bash
cd weather-monitoring
```

3. Create a virtual environment (optional but recommended).

```bash
python3 -m venv venv
source venv/bin/activate
```

## Usage

The project consists of two main scripts:

1. `data_collection.py`: This script fetches weather data using the open weather API and saves it to a .csv file.

Excute the python file with the API Key, the name of the city and the number of days as arguments:
```bash
python data_collection.py API_KEY CITY_NAME NUMBER_OF_DAYS
```
Note: All of these inputs should be seperated with a space. To input a city with spaces in between, use_an_underscore.

2. `data_visualization.py`: This script reads the .csv data and generates a graph using matplotlib.

Excute the python file with the path of the generated .CSV file as the argument:
```bash
python data_visualization.py PATH_OF_CSV_FILE
```
## Data Collection

To collect weather data, run the `data_collection.py` script. It will fetch the weather data for the current day and store it in a .csv file with the format 'weather_info_{city_name}_{current_date}.csv'. The data collection process will repeat automatically every 24 hours and apend the data in the existing file.     

Note: For continuous data collection, it is recommended to use a remote server or a cloud-based solution to keep the script running uninterrupted even if your local machine is turned off. Running the script on a remote server ensures that the data collection process remains active 24/7, providing consistent updates for the weather data. You can deploy the script on platforms like AWS, Google Cloud, or a virtual private server (VPS) for this purpose. Additionally, consider setting up scheduled execution or utilizing serverless architectures for efficient and automated data collection.

## Data Visualization

To visualize the collected weather data, run the `data_visualization.py` script. It will read the .csv file and generate a graph displaying the weather trends over time in 'temperature_plot.png'.

## Contributing

Contributions to this project are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

When contributing, please adhere to the existing code style and ensure that your changes do not break the existing functionality.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
