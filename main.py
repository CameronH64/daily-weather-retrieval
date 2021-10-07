"""
Cameron Holbrook

Project Description:

This program will grab current weather information
and store it in a local MySQL database.


Outline:

    Import statements
    Load dotenv for API key
    Setup the Tkinter window
    Python functions
    Create GUI elements (Label, Entry, etc.)
    Run the Tkinter mainloop.
    Reference materials


"""
import time

import requests             # Used to call the HTTP API.
from dotenv import load_dotenv      # Used to store the API key
import os                   # Used to access environmental variables, and my API key.
import pprint               # Simply prints out .json output in a much neater format.
import mysql.connector      # Used to run SQL commands in Python
from tkinter import *
# from PIL import ImageTk, Image
# import datetime

# dotenv, for environment variables and protection of API key.
load_dotenv()

# Setup the Tkinter window.
root = Tk()
root.geometry("360x300")
root.resizable(False, False)         # (x, y)
root.title("Daily Weather Retrieval Tool")


# Plain OpenWeatherMap API calls
# https:/api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
OWMCity = "http:/api.openweathermap.org/data/2.5/weather?q={}&appid={}"
# https:/api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}
OWMCityID = "http:/api.openweathermap.org/data/2.5/weather?id={}&appid={}"
# https:/api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
OWMCoordinates = "http:/api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
# https:/api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}
OWMZipCode = "http:/api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}"

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

# Will call the OWM API, and return the API call weather data
def OWMCall(choice):

    if choice == "City":
        cityName = input("Enter a city to find its weather: ")

        url = OWMCity.format(cityName, os.getenv("API_KEY"))
        result = requests.get(url)
        data = result.json()

        return data

    elif choice == "City ID":
        print("Hey, listen! City ID!")

    elif choice == "Coordinates":
        print("Hey, listen! Coordinates!")

    elif choice == "ZIP Code":
        print("Hey, listen! ZIP Code!")

# Testing City ID's
# Greenbrier, TN:        4626286
# Greenbrier, AR:        4113067

def searchButtonClicked():
    return searchEntry.get()


# ================= CREATE ELEMENTS FOR GUI =================

# ENTRY box, search box
searchEntry = Entry(root, width=30)
searchEntry.grid(row=1, column=0)


# LABEL widget for API call return
output = Label(root, text="Weather API call goes here.")
output.grid(row=2, column=0)

# Use a scrollbar?

# Weather details to display:

# main.temp
# main.feels_like
# main.humidity
# main.temp_min
# main.temp_max

# wind.speed
# wind.deg
# clouds.all

# rain.1h
# rain.3h

# snow.1h
# snow.3h

# sys.country
# sys.sunrise
# sys.sunset
# id
# name

# BUTTON, submission button
submissionButton = Button(root, text="Search", command=lambda: searchButtonClicked())
submissionButton.grid(row=1, column=1)

# RADIO buttons, search choices

searchChoices = IntVar()        # This function allows Tkinter to keep track of changes over time to this variable. More special than a standard Python variable.
searchChoices.set(1)            # Set the default value of the group of radio buttons.

# Will need to have "variable" and "value".
Radiobutton(root, text="City",                      variable=searchChoices, value=1).grid(row=2, column=1, sticky=W)      # (Offset so it's easier to see).
Radiobutton(root, text="City ID",                   variable=searchChoices, value=2).grid(row=3, column=1, sticky=W)
Radiobutton(root, text="Geographic\nCoordinates",   variable=searchChoices, value=3).grid(row=4, column=1, sticky=W)
Radiobutton(root, text="ZIP Code",                  variable=searchChoices, value=4).grid(row=5, column=1, sticky=W)

# LABEL, temperature units choice
temperatureUnits = Label(root, text="Temperature Units:")
temperatureUnits.grid(row=6, column=1)

# RADIO buttons, temperature choice
temperatureUnits = IntVar()        # This function allows Tkinter to keep track of changes over time to this variable. More special than a standard Python variable.
temperatureUnits.set(1)            # Set the default value of the group of radio buttons.

Radiobutton(root, text="Fahrenheit",                variable=temperatureUnits, value=1).grid(row=7, column=1, sticky=W)      # (Offset so it's easier to see).
Radiobutton(root, text="Celsius",                   variable=temperatureUnits, value=2).grid(row=8, column=1, sticky=W)

# BUTTON, save to database (will use mysql-connector-python)
saveButton = Button(root, text="Save to\nlocal database", command=lambda: searchButtonClicked())
saveButton.grid(row=9, column=1)

# Activate Tkinter's mainloop window
root.mainloop()


# ================= REFERENCE MATERIALS =================

# Basically, all Tkinter is:

# from tkinter import *
# root = Tk()
# myLabel = Label(root, text="Hey, listen!")
# myLabel.grid()        # Could also use the simpler pack system.
# root.mainloop()

# e.get() will return the contents in the text field.

# Code to convert UNIX time to actual time.
# timestamp = datetime.datetime.fromtimestamp(1500000000)
# print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))