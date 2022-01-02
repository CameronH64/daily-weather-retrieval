"""
Cameron Holbrook

Project Description:

This program will grab current weather information
and store it in a local MySQL database.

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

# Set up the Tkinter window.
root = Tk()
root.geometry("360x300")
root.resizable(False, False)         # (x, y)
root.title("Daily Weather Retrieval Tool")

def APICall():

	cityName = input("Enter a city: ")

	# Do Open Weather Map API call.
	callString = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(cityName, os.getenv("APIKey"))
	requestReturn = requests.get(callString)
	data = requestReturn.json()

	print(data['main']['temp'])


def askCity():
	return input("Enter a city: ")


def testCall(cityName):

	return 0


# Testing City ID's
# Greenbrier, TN:        4626286
# Greenbrier, AR:        4113067

def saveButtonClicked():
	cityName = searchEntry.get()

	# Do Open Weather Map API call.
	callString = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(cityName, os.getenv("APIKey"))
	requestReturn = requests.get(callString)
	data = requestReturn.json()

	pprint.pprint(data)


	# I now have data, which holds the information I need.
	# Put in a large try catch?

	# clouds	varchar(10),
	try:
		clouds = data['snow']['snow.1h']
	except Exception:
		print("Error: Hasn't snowed yet.")

	# humidity      varchar(20)

	# temp_min      float

	# temp_max      float

	# main_temp     float

	# feels_like	float

	# wind_gust     float

	# wind_speed    float

	# wind_deg      int

	# rain_1h       float

	# rain_3h       float

	# snow_1h       float

	# snow_3h       float

	# weather_description       varchar(20)

	# weather_icon				varchar(5)

	# weather_main				varchar(20)

	# city_ID					varchar(20)

	# city_Name					varchar(20)

	# date_calculated			date

	# timezone		int

	# latitude		float

	# longitude		float

	# sunrise		varchar(20)

	# sunset		varchar(20)

	# country		varchar(30)

	# main_pressure	int

	# grnd_level	int

	# sea_level	int


	# For testing purposes.
	print()

# ================= CREATE ELEMENTS FOR GUI =================

# Search box
searchEntry = Entry(root, width=30)
searchEntry.grid(row=1, column=0)

# API call return box
# output = Label(root, text="Weather API call goes here.")
# output.grid(row=2, column=0)

# Search button
searchButton = Button(root, text="Save to Database", command=lambda: saveButtonClicked())
searchButton.grid(row=1, column=1)

# Search radio buttons
# searchChoices = IntVar()        # This function allows Tkinter to keep track of changes over time to this variable. More special than a standard Python variable.
# searchChoices.set(1)            # Set the default value of the group of radio buttons.
#
# Radiobutton(root, text="City",                      variable=searchChoices, value=1).grid(row=2, column=1, sticky=W)
# Radiobutton(root, text="City ID",                   variable=searchChoices, value=2).grid(row=3, column=1, sticky=W)
# Radiobutton(root, text="Geographic\nCoordinates",   variable=searchChoices, value=3).grid(row=4, column=1, sticky=W)
# Radiobutton(root, text="ZIP Code",                  variable=searchChoices, value=4).grid(row=5, column=1, sticky=W)


# Temperature units choice label
# temperatureUnits = Label(root, text="Temperature Units:")
# temperatureUnits.grid(row=6, column=1)


# Temperature radio buttons

# temperatureUnits = IntVar()        # This function allows Tkinter to keep track of changes over time to this variable. More special than a standard Python variable.
# temperatureUnits.set(1)            # Set the default value of the group of radio buttons.
#
# Radiobutton(root, text="Fahrenheit",                variable=temperatureUnits, value=1).grid(row=7, column=1, sticky=W)      # (Offset so it's easier to see).
# Radiobutton(root, text="Celsius",                   variable=temperatureUnits, value=2).grid(row=8, column=1, sticky=W)


# ===================== END CREATE ELEMENTS FOR GUI =====================

# (weather_database is hardcoded).

# MySQL connector setup
db = mysql.connector.connect(

	host="localhost",
	user="root",
	password=os.getenv("rootPassword"),

	# Can I check database here? Do testing later...
	database="weather_database"

)

# Create the cursor for executing SQL commands.
mycursor = db.cursor()

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