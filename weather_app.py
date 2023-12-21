import requests
import sys

# API key from OpenWeatherMap (replace with your own API key)
api_key = "xxxxxxxxxxxxxxxxxxxxxxx"
# api_key = "API KEY YOU GET FROM YOUR SERVICE FOR EX. : https://openweathermap.org/"

# Function to get geographic coordinates (latitude and longitude) for a city
def get_coordinates(city_name, api_key):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}")
    return response.json()

# Function to get weather data for a given city using coordinates
def get_weather_data(lat, lon, api_key, unit):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={unit}")
    return response.json()

# Function to validate user's measurement unit selection
def validate_measurement_unit(measurement):
    return measurement == "M" or measurement == "I"

# Function to display weather information
def display_weather_info(city_name, weather_forecast, weather_temperature, unit):
    if unit == "M":
        print(f"City Name: {city_name} || Weather Forecast: {weather_forecast} || Weather Temperature: {weather_temperature}°C")
    elif unit == "I":
        print(f"City Name: {city_name} || Weather Forecast: {weather_forecast} || Weather Temperature: {weather_temperature}°F")

def main():
    # Get user input for the city
    user_input = input("Enter a valid city: ").strip().capitalize()

    # Get geographic coordinates for the given city
    geo_data = get_coordinates(user_input, api_key)

    # Extract latitude and longitude from the response
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    # User selects measurement units (imperial or metric)
    print("\nSelect one: IMPERIAL or METRIC")
    print("\nFor Metric enter: M")
    print("For Imperial enter: I")
    measurement = input("Enter: ").strip().upper()

    counter = 0

    # Validate the user's measurement unit selection
    while counter < 4 and not validate_measurement_unit(measurement):
        counter += 1
        print("\nINVALID SELECTION!")
        measurement = input("Enter again: ").strip().upper()

    # Exit the program if the user enters an invalid selection multiple times
    if counter == 3:
        print("\nToo many wrong enters!")
        sys.exit(1)

    # Set the unit for the OpenWeatherMap API request based on the user's selection
    unit = "metric" if measurement == "M" else "imperial"

    # Get weather data for the specified city and coordinates
    weather_data = get_weather_data(lat, lon, api_key, unit)

    # Extract relevant information from the weather data
    city_name = weather_data["name"]
    weather_forecast = weather_data["weather"][0]["main"]
    weather_temperature = round(weather_data["main"]["temp"])

    # Display the weather information based on the selected measurement unit
    display_weather_info(city_name, weather_forecast, weather_temperature, measurement)

if __name__ == "__main__":
    main()