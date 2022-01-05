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
import datetime

# dotenv, for environment variables and protection of API key.
load_dotenv()

# Set up the Tkinter window.
root = Tk()
root.geometry("360x300")
root.resizable(False, False)         # (x, y)
root.title("Daily Weather Retrieval Tool")


def doAPICall(cityName):

	# Do Open Weather Map API call.
	callString = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(cityName, os.getenv("APIKey"))
	requestReturn = requests.get(callString)

	return requestReturn.json()


def saveButtonClicked():

	cityName = searchEntry.get()
	data = doAPICall(cityName)

	# Convert the time calculated.
	dt = data['dt']
	dateCalculated = str(datetime.datetime.fromtimestamp(dt))
	print("Date Calculated: \t\t" + str(dateCalculated))

	# If row with this datetime exists,
	# Print error message.
	# Else, insert data.

	# Do first SQL insert with only this calculation date.
	insertCalculationDateRow = ("insert into weather_details(date_calculated) "
								"values('2022-01-04 09:23:48');")

	mycursor.execute(insertCalculationDateRow, dateCalculated)
	db.commit()

	# For debugging purposes
	pprint.pprint(data)
	print()
	print()


	# clouds	varchar(10),
	try:
		clouds = data['clouds']['all']
	except Exception:
		print("API Call Error: No clouds.")
	else:
		# Save to database code here.
		print("Clouds: \t\t\t\t" + str(clouds) + "%")

	# humidity      varchar(20)
	try:
		humidity = data['main']['humidity']
	except Exception:
		print("API Call Error: No humidity.")
	else:
		# Save to database code here.
		print("Humidity: \t\t\t\t" + str(humidity) + "%")

	# temp_min      float
	try:
		temp_min = data['main']['temp_min']
	except Exception:
		print("API Call Error: No minimum temperature.")
	else:
		# Save to database code here.
		print("Minimum temperature: \t" + str(temp_min) + " degrees fahrenheit")

	# temp_max      float
	try:
		temp_max = data['main']['temp_max']
	except Exception:
		print("API Call Error: No maximum temperature.")
	else:
		# Save to database code here.
		print("Maximum temperature: \t" + str(temp_max) + " degrees fahrenheit")

	# main_temp     float
	try:
		temp = data['main']['temp']
	except Exception:
		print("API Call Error: No maximum temperature.")
	else:
		# Save to database code here.
		print("Temperature: \t\t\t" + str(temp) + " degrees fahrenheit")

	# feels_like	float
	try:
		feels_like = data['main']['feels_like']
	except Exception:
		print("API Call Error: No feels-like temperature.")
	else:
		# Save to database code here.
		print("Feels like: \t\t\t" + str(feels_like) + " degrees fahrenheit")

	# wind_gust     float
	try:
		gust = data['wind']['gust']
	except Exception:
		print("API Call Error: No wind gust measurement.")
	else:
		# Save to database code here.
		print("Wind gust: \t\t\t\t" + str(gust) + " miles per hour")

	# wind_speed    float
	try:
		speed = data['wind']['speed']
	except Exception:
		print("API Call Error: No wind speed measurement.")
	else:
		# Save to database code here.
		print("Wind speed: \t\t\t" + str(speed) + " miles per hour")

	# wind_deg      int
	try:
		deg = data['wind']['deg']
	except Exception:
		print("API Call Error: No wind direction.")
	else:
		# Save to database code here.
		print("Wind Degree: \t\t\t" + str(deg) + " meteorological degrees")

	# rain_1h       float
	try:
		rain_1h = data['rain']['1h']
	except Exception:
		print("API Call Error: No recent 1 hour rain measurement.")
	else:
		# Save to database code here.
		print("Rain 1h: \t\t\t" + str(rain_1h) + " mm")

	# rain_3h       float
	try:
		rain_3h = data['rain']['3h']
	except Exception:
		print("API Call Error: No recent 3 hour rain measurement.")
	else:
		# Save to database code here.
		print("Rain 3h: \t\t\t" + str(rain_3h) + " mm")

	# snow_1h       float
	try:
		snow_1h = data['snow']['1h']
	except Exception:
		print("API Call Error: No recent 1 hour snow measurement.")
	else:
		# Save to database code here.
		print("Snow 1h: \t\t\t\t" + str(snow_1h) + " mm")

	# snow_3h       float
	try:
		snow_3h = data['snow']['3h']
	except Exception:
		print("API Call Error: No recent 3 hour snow measurement.")
	else:
		# Save to database code here.
		print("Snow 3h: \t\t\t\t" + str(snow_3h) + " mm")

	# weather_description       varchar(20)
	try:
		description = data['weather'][0]['description']
	except Exception:
		print("API Call Error: No weather description.")
	else:
		# Save to database code here.
		print("Weather Description: \t" + str(description))

	# weather_icon				varchar(5)
	try:
		icon = data['weather'][0]['icon']
	except Exception:
		print("API Call Error: No weather icon.")
	else:
		# Save to database code here.
		print("Weather icon: \t\t\t" + str(icon))

	# weather_main				varchar(20)
	try:
		main = data['weather'][0]['main']
	except Exception:
		print("API Call Error: No weather main.")
	else:
		# Save to database code here.
		print("Weather Main: \t\t\t" + str(main))

	# city_ID					varchar(20)
	try:
		id = data['id']
	except Exception:
		print("API Call Error: No city id.")
	else:
		# Save to database code here.
		print("City ID: \t\t\t\t" + str(id))

	# city_Name					varchar(20)
	try:
		name = data['name']
	except Exception:
		print("API Call Error: No city name.")
	else:
		# Save to database code here.
		print("City Name: \t\t\t\t" + str(name))

	# date_calculated			date
	# Used to be here

	# timezone		int
	try:
		timezone = data['timezone']
	except Exception:
		print("API Call Error: No timezone.")
	else:
		# Save to database code here.
		print("Timezone: \t\t\t\t" + str(timezone))

	# latitude		float
	try:
		latitude = data['coord']['lat']
	except Exception:
		print("API Call Error: No latitude.")
	else:
		# Save to database code here.
		print("Latitude: \t\t\t\t" + str(latitude))

	# longitude		float
	try:
		longitude = data['coord']['lon']
	except Exception:
		print("API Call Error: No longitude.")
	else:
		# Save to database code here.
		print("Longitude: \t\t\t\t" + str(longitude))

	# sunrise		varchar(20)
	try:
		sunrise = data['sys']['sunrise']
	except Exception:
		print("API Call Error: No sunrise.")
	else:
		# Save to database code here.
		print("Sunrise: \t\t\t\t" + str(sunrise))

	# sunset		varchar(20)
	try:
		sunset = data['sys']['sunset']
	except Exception:
		print("API Call Error: No sunset.")
	else:
		# Save to database code here.
		print("Sunset: \t\t\t\t" + str(sunset))

	# country		varchar(30)
	try:
		country = data['sys']['country']
	except Exception:
		print("API Call Error: No country.")
	else:
		# Save to database code here.
		print("Country: \t\t\t\t" + str(country))

	# main_pressure	int
	try:
		pressure = data['sys']['pressure']
	except Exception:
		print("API Call Error: No pressure.")
	else:
		# Save to database code here.
		print("Pressure: \t\t" + str(pressure))

	# grnd_level	int
	try:
		grnd_level = data['sys']['grnd_level']
	except Exception:
		print("API Call Error: No grnd_level pressure.")
	else:
		# Save to database code here.
		print("Ground level pressure: \t\t" + str(grnd_level))

	# sea_level	int
	try:
		sea_level = data['sys']['sea_level']
	except Exception:
		print("API Call Error: No sea_level pressure.")
	else:
		# Save to database code here.
		print("Sea level pressure: \t\t" + str(sea_level))



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


# ===================== END CREATE ELEMENTS FOR GUI; START CODE=====================

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

db.close()

# ================= REFERENCE MATERIALS =================

# Testing City ID's
# Greenbrier, TN:        4626286
# Greenbrier, AR:        4113067

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