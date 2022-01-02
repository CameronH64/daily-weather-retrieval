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
	callString = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(cityName, os.getenv("APIKey"))
	requestReturn = requests.get(callString)
	data = requestReturn.json()

	pprint.pprint(data)
	print()			# For testing formatting purposes.
	print()

	# Next:
	# Decide what needs exception handling.
	# Write the save to database code
	# Will also need to factor in SQL datatypes


	# clouds	varchar(10),
	try:
		clouds = data['clouds']['all']
	except Exception:
		print("API Call Error: No clouds.")
	else:
		# Save to database code here.
		print(str(clouds) + "%")

	# humidity      varchar(20)
	try:
		humidity = data['main']['humidity']
	except Exception:
		print("API Call Error: No humidity.")
	else:
		# Save to database code here.
		print(str(humidity) + "%")

	# temp_min      float
	try:
		temp_min = data['main']['temp_min']
	except Exception:
		print("API Call Error: No minimum temperature.")
	else:
		# Save to database code here.
		print(str(temp_min) + " degrees fahrenheit")

	# temp_max      float
	try:
		temp_max = data['main']['temp_max']
	except Exception:
		print("API Call Error: No maximum temperature.")
	else:
		# Save to database code here.
		print(str(temp_max) + " degrees fahrenheit")

	# main_temp     float
	try:
		temp = data['main']['temp']
	except Exception:
		print("API Call Error: No maximum temperature.")
	else:
		# Save to database code here.
		print(str(temp) + " degrees fahrenheit")

	# feels_like	float
	try:
		feels_like = data['main']['feels_like']
	except Exception:
		print("API Call Error: No feels-like temperature.")
	else:
		# Save to database code here.
		print(str(feels_like) + " degrees fahrenheit")

	# wind_gust     float
	try:
		gust = data['wind']['gust']
	except Exception:
		print("API Call Error: No wind gust measurement.")
	else:
		# Save to database code here.
		print(str(gust) + " miles per hour")

	# wind_speed    float
	try:
		speed = data['wind']['speed']
	except Exception:
		print("API Call Error: No wind speed measurement.")
	else:
		# Save to database code here.
		print(str(speed) + " miles per hour")

	# wind_deg      int
	try:
		deg = data['wind']['deg']
	except Exception:
		print("API Call Error: No wind direction.")
	else:
		# Save to database code here.
		print(str(deg) + " meteorological degrees")

	# rain_1h       float
	try:
		rain_1h = data['rain']['1h']
	except Exception:
		print("API Call Error: No recent 1 hour rain measurement.")
	else:
		# Save to database code here.
		print(str(rain_1h) + " mm")

	# rain_3h       float
	try:
		rain_3h = data['rain']['3h']
	except Exception:
		print("API Call Error: No recent 3 hour rain measurement.")
	else:
		# Save to database code here.
		print(str(rain_3h) + " mm")

	# snow_1h       float
	try:
		snow_1h = data['snow']['1h']
	except Exception:
		print("API Call Error: No recent 1 hour snow measurement.")
	else:
		# Save to database code here.
		print(str(snow_1h) + " mm")

	# snow_3h       float
	try:
		snow_3h = data['snow']['3h']
	except Exception:
		print("API Call Error: No recent 3 hour snow measurement.")
	else:
		# Save to database code here.
		print(str(snow_3h) + " mm")

	# weather_description       varchar(20)
	try:
		description = data['weather']['description']
	except Exception:
		print("API Call Error: No weather description.")
	else:
		# Save to database code here.
		print(str(description))

	# weather_icon				varchar(5)
	try:
		icon = data['weather']['icon']
	except Exception:
		print("API Call Error: No weather icon.")
	else:
		# Save to database code here.
		print(str(icon) + " (this is the weather icon)")

	# weather_main				varchar(20)
	try:
		main = data['weather']['main']
	except Exception:
		print("API Call Error: No weather main.")
	else:
		# Save to database code here.
		print(str(main))

	# city_ID					varchar(20)
	try:
		id = data['id']
	except Exception:
		print("API Call Error: No city id.")
	else:
		# Save to database code here.
		print(str(id))

	# city_Name					varchar(20)
	try:
		name = data['name']
	except Exception:
		print("API Call Error: No city name.")
	else:
		# Save to database code here.
		print(str(name))

	# date_calculated			date
	try:
		dt = data['dt']
	except Exception:
		print("API Call Error: No calculation date.")
	else:
		# Save to database code here.
		print(str(dt))

	# timezone		int
	try:
		timezone = data['timezone']
	except Exception:
		print("API Call Error: No timezone.")
	else:
		# Save to database code here.
		print(str(timezone))

	# latitude		float
	try:
		latitude = data['coord']['lat']
	except Exception:
		print("API Call Error: No latitude.")
	else:
		# Save to database code here.
		print(str(latitude))

	# longitude		float
	try:
		longitude = data['coord']['lon']
	except Exception:
		print("API Call Error: No longitude.")
	else:
		# Save to database code here.
		print(str(longitude))

	# sunrise		varchar(20)
	try:
		sunrise = data['sys']['sunrise']
	except Exception:
		print("API Call Error: No sunrise.")
	else:
		# Save to database code here.
		print(str(sunrise))

	# sunset		varchar(20)
	try:
		sunset = data['sys']['sunset']
	except Exception:
		print("API Call Error: No sunset.")
	else:
		# Save to database code here.
		print(str(sunset))

	# country		varchar(30)
	try:
		country = data['sys']['country']
	except Exception:
		print("API Call Error: No country.")
	else:
		# Save to database code here.
		print(str(country))

	# main_pressure	int
	try:
		pressure = data['sys']['pressure']
	except Exception:
		print("API Call Error: No pressure.")
	else:
		# Save to database code here.
		print(str(pressure))

	# grnd_level	int
	try:
		grnd_level = data['sys']['grnd_level']
	except Exception:
		print("API Call Error: No grnd_level pressure.")
	else:
		# Save to database code here.
		print(str(grnd_level))

	# sea_level	int
	try:
		sea_level = data['sys']['sea_level']
	except Exception:
		print("API Call Error: No sea_level pressure.")
	else:
		# Save to database code here.
		print(str(sea_level))



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