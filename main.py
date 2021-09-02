import requests
from dotenv import load_dotenv
import os
import pprint
import mysql.connector

# dotenv, for environment variables and protection of API key.
load_dotenv()


def connectToDatabase():

    # (test_weather_database is hardcoded).

    # MySQL connector setup
    db = mysql.connector.connect(

        host="localhost", user="root",
        password=os.getenv("ROOT"),

        # Can I check database here? Do some testing...
        database="test_weather_database"

    )

    # Code to determine if database already exists here.

    # myCursor = db.cursor()          # Create a cursor object; this lets us use SQL commands.
    #
    # myCursor.execute("show databases;")
    # myCursor.execute("use database test_weather_database")

    # Test if an insert command works.
    # BIG IDEA! Design and implement the database FIRST!
    # THEN, have insert and delete commands from this python script!




# Store a city's weather data

def printWeatherData(data):

    # Print that weather data, for testing
    pprint.pprint(data)


def searchMethod():

    selection = input("Which would you like to do?\n\n1. City\n2. City ID\n\n")

    if selection == "1":        # Selection has to be a string because of the input!

        cityName = input("Enter a city name: ")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={os.getenv('API_KEY')}&units=imperial"
        result = requests.get(url)
        data = result.json()

        return data

    elif selection == "2":
        cityID = input("Enter a city ID: ")

        url = f"http://api.openweathermap.org/data/2.5/weather?id={cityID}&appid={os.getenv('API_KEY')}&units=imperial"
        result = requests.get(url)
        data = result.json()

        # Greenbrier, AR:           4626286
        # Also Greenbrier, AR?      4113067

        return data



def main():

    # connectToDatabase()

    # Loop to ask user what cities to collect weather data for.
    data = searchMethod()
    printWeatherData(data[main.temp])

    # print("Hey, listen!")       # Just so Python doesn't get mad at me.



if __name__ == '__main__':
    main()
