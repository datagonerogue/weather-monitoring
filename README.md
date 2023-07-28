# Weather Data Monitoring and Graphing

This Python project is designed to collect weather data for the current day, wait for 24 hours, collect data again, and repeat the process. The collected data is then stored in a .csv file for further analysis. Additionally, the project includes a script to visualize the data in a graph using the popular Python library, matplotlib.

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

## Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/weather-monitoring.git
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

4. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

The project consists of two main scripts:

1. `data_collection.py`: This script fetches weather data and saves it to a .csv file.
2. `data_visualization.py`: This script reads the .csv data and generates a graph using matplotlib.

## Data Collection

To collect weather data, run the `data_collection.py` script. It will fetch the weather data for the current day and store it in a .csv file. The data collection process will repeat automatically every 24 hours.     

```bash
python data_collection.py    
```
Note: For continuous data collection, it is recommended to use a remote server or a cloud-based solution to keep the script running uninterrupted even if your local machine is turned off. Running the script on a remote server ensures that the data collection process remains active 24/7, providing consistent updates for the weather data. You can deploy the script on platforms like AWS, Google Cloud, or a virtual private server (VPS) for this purpose. Additionally, consider setting up scheduled execution or utilizing serverless architectures for efficient and automated data collection.

## Data Visualization

To visualize the collected weather data, run the `data_visualization.py` script. It will read the .csv file and generate a graph displaying the weather trends over time.

```bash
python data_visualization.py
```

## Contributing

Contributions to this project are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

When contributing, please adhere to the existing code style and ensure that your changes do not break the existing functionality.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
