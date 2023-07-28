# Python Weather Forecast Visualization 
# ***IN DEVELOPMENT***

<!-- ![Weather Forecast Visualization](example image here) -->

This Python-based weather forecast visualization project aims to provide interactive plots showcasing temperature, precipitation, and wind patterns using the popular Matplotlib library. By leveraging this tool, users can gain insights into the weather forecast data with ease.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Weather forecasting plays a crucial role in our daily lives, whether it's planning outdoor activities or preparing for potential weather hazards. This project offers a straightforward Python solution to visualize weather forecast data in an interactive and user-friendly manner. The primary objective is to empower users to make informed decisions based on the forecast data.

## Installation

To get started with the weather forecast visualization project, follow the steps below:

1. Clone the repository:

```
git clone https://github.com/CTM-Giorno/forecast-visualizer.git
cd forecast-visualizer
```

2. Set up a virtual environment (optional but recommended):

```
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Obtain an openweather data API key. (Ex. [OpenWeather APIs.](https://openweathermap.org/api))
## Usage

Once the project is set up and you have acquired the weather forecast data, follow these steps to visualize the weather patterns:

1. Run the main Python script:

```
python api_to_dataframe.py [YOUR_API_KEY] [LOCATION] [NUMBER_OF_DAYS]
```

2. The script will prompt you to input the API key and Location for the forcast.
    
3. After processing the data from the open weather, the data will be displayed to you on the terminal. Also, The data will be saved on a .csv gile while on the working directory.

4. The code will pause for a day. After 24 Hours it will ping the API again (no need for any input) repeat the step 3.

## Features

- **Interactive Visualization**: The project offers interactive plots, allowing users to explore weather forecast data conveniently.

- **Temperature Plot**: Visualize temperature patterns over time, helping users understand temperature fluctuations.

### Upcomimng Features

- **Precipitation Plot**: Understand precipitation levels and patterns with an easy-to-read precipitation plot.

- **Wind Pattern Plot**: The wind pattern plot shows the direction and intensity of the wind, providing insights into weather conditions.

- **Customization**: Users can customize the plots based on their preferences and requirements.

## Contributing

Contributions to this weather forecast visualization project are welcome! If you want to enhance the functionality, fix bugs, or add new features, follow these steps:

1. Fork the repository.

2. Create a new branch with a descriptive name.

3. Make your changes and commit them.

4. Push the changes to your fork.

5. Submit a pull request, explaining your changes in detail.

We appreciate your contributions to making this project better.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy weather forecasting and visualization! If you encounter any issues or have suggestions, feel free to create an issue in the repository. Enjoy exploring the weather data with our interactive plots!
