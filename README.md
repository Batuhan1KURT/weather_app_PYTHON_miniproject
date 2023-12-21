# City Weather Info

This Python script uses the OpenWeatherMap API to retrieve and display current weather information for a given city. The script allows users to input a city, choose between metric and imperial units, and then provides weather details such as forecast and temperature.



## Usage
1. Open a terminal and navigate to the directory where the script is located.
2. Run the script by entering the following command:
3. You will be prompted to enter a valid city name.
5. After entering the city name, you will be asked to select the measurement unit:
    - Enter `M` for METRIC (Celcius).
    - Enter `I` for IMPERIAL (Fahrenheit).
5. The script will then display the current weather information for the specified city.

## Functionality
- **Geographic Coordinates Retrieval:**
- The script uses the OpenWeatherMap API to fetch the geographic coordinates (latitude and longitude) for the given city.

- **Weather Data Retrieval:**
- With the obtained coordinates, the script makes a second API call to fetch current weather data, including forecast and temperature.

- **User Input Validation:**
- The script validates the user's input for the measurement unit, allowing only `M` (METRIC) or `I` (IMPERIAL).

- **Display Weather Information:**
- The script displays relevant weather information, including the city name, weather forecast, and temperature, based on the selected measurement unit.
