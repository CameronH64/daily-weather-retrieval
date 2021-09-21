import requests             # Used to call the HTTP API.
from dotenv import load_dotenv      # Used to store the API key
import os                   # Used to access environmental variables, and my API key.
import pprint               # Simply prints out .json output in a much neater format.
import mysql.connector      # Used to run SQL commands in Python
# Use Tkinter or Kivy as a quick and dirty GUI?

# dotenv, for environment variables and protection of API key.
load_dotenv()

# Ignoring this for now; getting OWM stuff down first.
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

def searchByCity():

    cityName = input("Enter a city to find its weather: ")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={os.getenv('API_KEY')}&units=imperial"
    result = requests.get(url)
    data = result.json()

    return data

def searchByState():

    stateName = input("Enter a state to find its weather: ")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={stateName}&appid={os.getenv('API_KEY')}&units=imperial"
    result = requests.get(url)
    data = result.json()

    return data

def searchByCountry():

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

def searchByCityCode():

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


# Greenbrier, AR:           4626286
# Also Greenbrier, AR?      4113067


###################### CODE STARTS HERE ######################

print("Pick a weather search option: ")
print("1. Search by city.")
print("2. Search by state.")
print("3. Search by country.")
print("4. Search by city code (according to OpenWeatherMap's code list).")


choice = input()

if choice == "1":
    searchByCity()


elif choice == "2":
    searchByState()


elif choice == "3":
    searchByCountry()


elif choice == "4":
    searchByCityCode()


print("Program has ended.")


