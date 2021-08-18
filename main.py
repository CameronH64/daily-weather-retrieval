import requests
from dotenv import load_dotenv
import os
import pprint
import mysql.connector

########## SETUP ##########

# dotenv, for environment variables and protection of API key.
load_dotenv()

########## END SETUP ##########

def connectToDatabase():

    # MySQL connector setup
    db = mysql.connector.connect(

        host="localhost", user="root",
        password=os.getenv("ROOT"),
        database="test_weather_database"

    )

    myCursor = db.cursor()

    myCursor.execute("show databases;")

    myCursor.execute("use database test_weather_database")


def printWeatherData(data):

    # Print that weather data, for testing
    pprint.pprint(data)


def main():

    # connectToDatabase()

    """Main, where the program starts."""

    # Main program start

    selection = input("Which would you like to do?\n\n1. City\n2. City ID\n\n")

    if selection == 1:

        cityName = input("Enter a city name: ")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={os.getenv('API_KEY')}&units=imperial"
        result = requests.get(url)

        # Store that URL into a printable variable
        data = result.json()

        printWeatherData(data)


    else:
        cityID = input("Enter a city ID: ")

        url2 = f"http://api.openweathermap.org/data/2.5/weather?id={cityID}&appid={os.getenv('API_KEY')}&units=imperial"
        result = requests.get(url2)

        # Store that URL into a printable variable
        data = result.json()

        # Original: 4626286
        # Secondary? 4113067

        printWeatherData(data)



if __name__ == '__main__':
    main()
