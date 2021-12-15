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


def connectToDatabase():

	# (test_weather_database is hardcoded).

	# MySQL connector setup
	db = mysql.connector.connect(

		host="localhost",
		user="root",
		password=os.getenv("rootPassword"),

		# Can I check database here? Do testing later...
		database="weather_database"

	)

	# Create the cursor for executing SQL commands.
	cursor = db.cursor()


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

def searchButtonClicked():
	cityName = searchEntry.get()

	# Do Open Weather Map API call.
	callString = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(cityName, os.getenv("APIKey"))
	requestReturn = requests.get(callString)
	data = requestReturn.json()

	# For testing purposes.
	pprint.pprint(data)


def saveToDatabase():
	print()
	# Have cursor statements in here
	# data['main']['temp'] and assignment and stuff like that.


# ================= CREATE ELEMENTS FOR GUI =================

# Search box
searchEntry = Entry(root, width=30)
searchEntry.grid(row=1, column=0)

# API call return box
output = Label(root, text="Weather API call goes here.")
output.grid(row=2, column=0)

# Search button
searchButton = Button(root, text="Search", command=lambda: searchButtonClicked())
searchButton.grid(row=1, column=1)

# Search radio buttons
searchChoices = IntVar()        # This function allows Tkinter to keep track of changes over time to this variable. More special than a standard Python variable.
searchChoices.set(1)            # Set the default value of the group of radio buttons.

Radiobutton(root, text="City",                      variable=searchChoices, value=1).grid(row=2, column=1, sticky=W)      # (Offset so it's easier to see).
Radiobutton(root, text="City ID",                   variable=searchChoices, value=2).grid(row=3, column=1, sticky=W)
Radiobutton(root, text="Geographic\nCoordinates",   variable=searchChoices, value=3).grid(row=4, column=1, sticky=W)
Radiobutton(root, text="ZIP Code",                  variable=searchChoices, value=4).grid(row=5, column=1, sticky=W)


# Temperature units choice label
temperatureUnits = Label(root, text="Temperature Units:")
temperatureUnits.grid(row=6, column=1)


# Temperature radio buttons

temperatureUnits = IntVar()        # This function allows Tkinter to keep track of changes over time to this variable. More special than a standard Python variable.
temperatureUnits.set(1)            # Set the default value of the group of radio buttons.

Radiobutton(root, text="Fahrenheit",                variable=temperatureUnits, value=1).grid(row=7, column=1, sticky=W)      # (Offset so it's easier to see).
Radiobutton(root, text="Celsius",                   variable=temperatureUnits, value=2).grid(row=8, column=1, sticky=W)


# Save to database button
saveButton = Button(root, text="Save to\nlocal database", command=lambda: saveToDatabase())
saveButton.grid(row=9, column=1)

# ===================== END CREATE ELEMENTS FOR GUI =====================


root.mainloop()

connectToDatabase()



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