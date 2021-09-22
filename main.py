import requests             # Used to call the HTTP API.
from dotenv import load_dotenv      # Used to store the API key
import os                   # Used to access environmental variables, and my API key.
# import pprint               # Simply prints out .json output in a much neater format.
import mysql.connector      # Used to run SQL commands in Python
from tkinter import *
from PIL import ImageTk, Image

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


# OpenWeatherMap's functions

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


#====================== CODE STARTS HERE ============================

# GUI setup code here

root = Tk()

# Backend code here

# print("Pick a weather search option: ")
# print("1. Search by city.")
# print("2. Search by state.")
# print("3. Search by country.")
# print("4. Search by city code (according to OpenWeatherMap's code list).")
#
#
# choice = input()

def searchButtonClicked():
    response = fieldEntry.get()
    return response


question = Label(root, text="Enter a city: ")
question.grid(row=0, column=0)

fieldEntry = Entry(root, width=40)
fieldEntry.grid(row=1, column=0)

submissionButton = Button(root, text="Search", command=lambda: searchButtonClicked())
submissionButton.grid(row=1, column=1)

answer = searchButtonClicked()
print(answer + "Hey, listen!")


# print("Program has ended.")

root.mainloop()



# Tkinter documentation: https://docs.python.org/3/library/tk.html

# Basically, all Tkinter is:

# from tkinter import *
# root = Tk()
# myLabel = Label(root, text="Hey, listen!")
# myLabel.pack()        # Can also use grid system.
# root.mainloop()

