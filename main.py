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
root.geometry("480x300")

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
searchEntry = Entry(root, width=40)
searchEntry.grid(row=1, column=0)


# LABEL widget for API call return
output = Label(root, wraplength=500)
output.grid(row=2, column=0)


# BUTTON, submission button
submissionButton = Button(root, text="Search", command=lambda: searchButtonClicked())
submissionButton.grid(row=1, column=1)


# RADIO buttons, search choices


# LABEL, units choice


# RADIO buttons, temperature choice


# BUTTON, save to database


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