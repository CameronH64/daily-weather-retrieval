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
root.geometry("360x300+1400+600")
root.resizable(False, False)         # (x, y)
root.title("Daily Weather Retrieval Tool")


def doAPICall(cityName):

	# Do Open Weather Map API call.
	callString = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(cityName, os.getenv("APIKey"))
	requestReturn = requests.get(callString)

	return requestReturn.json()


def saveButtonClicked():

	# Do the API call
	cityName = searchEntry.get()
	data = doAPICall(cityName)

	# Convert the time calculated.
	dt = data['dt']
	dateCalculated = str(datetime.datetime.fromtimestamp(dt))
	cityName = data['name']											# Probably need this code to make formatting of city names in database consistent.
	# print("Date Calculated: \t\t" + str(dateCalculated))			# Still may need for testing.
	# dateCalculated = str(dateCalculated)

	rowDuplicationCheckQuery = "SELECT EXISTS(SELECT * FROM weather_details " \
							   "WHERE date_calculated='%s' AND city_name='%s');" % (dateCalculated, cityName)
	mycursor.execute(rowDuplicationCheckQuery)

	rowExistsList = mycursor.fetchall()
	# print("Row check: " + str(rowExistsList))		# For debugging purposes.

	if 0 in rowExistsList[0]:

		# It's okay to always assume this is allowed to run because it's been given the go ahead with the row duplication checking code above.
		insertDateAndCity = "INSERT INTO weather_details (date_calculated, city_name) " \
							"VALUES ('%s','%s');" % (dateCalculated, cityName)  # Key code!
		mycursor.execute(insertDateAndCity)
		db.commit()

		# clouds	varchar(10),
		try:
			clouds = int(data['clouds']['all'])
		except Exception:
			print("API Call Error: No clouds.")
		else:
			insertClouds = "UPDATE weather_details " \
						"SET clouds = '%s' WHERE date_calculated='%s' and city_name='%s';" % (clouds, dateCalculated, cityName)
			mycursor.execute(insertClouds)
			db.commit()

			print("Clouds: \t\t\t\t" + str(clouds) + "%")

		# humidity      varchar(20)
		try:
			humidity = data['main']['humidity']
		except Exception:
			print("API Call Error: No humidity.")
		else:
			insertTempMin = "UPDATE weather_details " \
						"SET humidity = '%s' WHERE date_calculated='%s' and city_name='%s';" % (humidity, dateCalculated, cityName)
			mycursor.execute(insertTempMin)
			db.commit()
			print("Humidity: \t\t\t\t" + str(humidity) + "%")

		# temp_min      float
		try:
			temp_min = data['main']['temp_min']
		except Exception:
			print("API Call Error: No minimum temperature.")
		else:
			# Save to database code here.
			insertTempMin = "UPDATE weather_details " \
						"SET temp_min = '%s' WHERE date_calculated='%s' and city_name='%s';" % (temp_min, dateCalculated, cityName)
			mycursor.execute(insertTempMin)
			db.commit()
			print("Minimum temperature: \t" + str(temp_min) + " degrees fahrenheit")

		# temp_max      float
		try:
			temp_max = data['main']['temp_max']
		except Exception:
			print("API Call Error: No maximum temperature.")
		else:
			# Save to database code here.
			insertTempMax = "UPDATE weather_details " \
						"SET temp_max = '%s' WHERE date_calculated='%s' and city_name='%s';" % (temp_max, dateCalculated, cityName)
			mycursor.execute(insertTempMax)
			db.commit()
			print("Maximum temperature: \t" + str(temp_max) + " degrees fahrenheit")

		# main_temp     float
		try:
			temp = data['main']['temp']
		except Exception:
			print("API Call Error: No maximum temperature.")
		else:
			# Save to database code here.
			insertTemp = "UPDATE weather_details " \
						"SET main_temp = '%s' WHERE date_calculated='%s' and city_name='%s';" % (temp, dateCalculated, cityName)
			mycursor.execute(insertTemp)
			db.commit()
			print("Temperature: \t\t\t" + str(temp) + " degrees fahrenheit")

		# feels_like	float
		try:
			feels_like = data['main']['feels_like']
		except Exception:
			print("API Call Error: No feels-like temperature.")
		else:
			# Save to database code here.
			insertFeelsLike = "UPDATE weather_details " \
						"SET feels_like = '%s' WHERE date_calculated='%s' and city_name='%s';" % (feels_like, dateCalculated, cityName)
			mycursor.execute(insertFeelsLike)
			db.commit()
			print("Feels like: \t\t\t" + str(feels_like) + " degrees fahrenheit")

		# wind_gust     float
		try:
			gust = data['wind']['gust']
		except Exception:
			print("API Call Error: No wind gust measurement.")
		else:
			# Save to database code here.
			insertWindGust = "UPDATE weather_details " \
						"SET feels_like = '%s' WHERE date_calculated='%s' and city_name='%s';" % (gust, dateCalculated, cityName)
			mycursor.execute(insertWindGust)
			db.commit()
			print("Wind gust: \t\t\t\t" + str(gust) + " miles per hour")

		# wind_speed    float
		try:
			speed = data['wind']['speed']
		except Exception:
			print("API Call Error: No wind speed measurement.")
		else:
			# Save to database code here.
			insertWindSpeed = "UPDATE weather_details " \
						"SET wind_speed = '%s' WHERE date_calculated='%s' and city_name='%s';" % (speed, dateCalculated, cityName)
			mycursor.execute(insertWindSpeed)
			db.commit()
			print("Wind speed: \t\t\t" + str(speed) + " miles per hour")

		# wind_deg      int
		try:
			deg = data['wind']['deg']
		except Exception:
			print("API Call Error: No wind direction.")
		else:
			# Save to database code here.
			insertWindDegree = "UPDATE weather_details " \
						"SET wind_deg = '%s' WHERE date_calculated='%s' and city_name='%s';" % (deg, dateCalculated, cityName)
			mycursor.execute(insertWindDegree)
			db.commit()
			print("Wind Degree: \t\t\t" + str(deg) + " meteorological degrees")

		# rain_1h       float
		try:
			rain_1h = data['rain']['1h']
		except Exception:
			print("API Call Error: No recent 1 hour rain measurement.")
		else:
			# Save to database code here.
			insertRain1h = "UPDATE weather_details " \
						"SET rain_1h = '%s' WHERE date_calculated='%s' and city_name='%s';" % (rain_1h, dateCalculated, cityName)
			mycursor.execute(insertRain1h)
			db.commit()
			print("Rain 1h: \t\t\t" + str(rain_1h) + " mm")

		# rain_3h       float
		try:
			rain_3h = data['rain']['3h']
		except Exception:
			print("API Call Error: No recent 3 hour rain measurement.")
		else:
			# Save to database code here.
			insertRain3h = "UPDATE weather_details " \
						"SET rain_3h = '%s' WHERE date_calculated='%s' and city_name='%s';" % (rain_3h, dateCalculated, cityName)
			mycursor.execute(insertRain3h)
			db.commit()
			print("Rain 3h: \t\t\t" + str(rain_3h) + " mm")

		# snow_1h       float
		try:
			snow_1h = data['snow']['1h']
		except Exception:
			print("API Call Error: No recent 1 hour snow measurement.")
		else:
			# Save to database code here.
			insertSnow1h = "UPDATE weather_details " \
						"SET snow_1h = '%s' WHERE date_calculated='%s' and city_name='%s';" % (snow_1h, dateCalculated, cityName)
			mycursor.execute(insertSnow1h)
			db.commit()
			print("Snow 1h: \t\t\t\t" + str(snow_1h) + " mm")

		# snow_3h       float
		try:
			snow_3h = data['snow']['3h']
		except Exception:
			print("API Call Error: No recent 3 hour snow measurement.")
		else:
			# Save to database code here.
			insertSnow3h = "UPDATE weather_details " \
						"SET snow_3h = '%s' WHERE date_calculated='%s' and city_name='%s';" % (snow_3h, dateCalculated, cityName)
			mycursor.execute(insertSnow3h)
			db.commit()
			print("Snow 3h: \t\t\t\t" + str(snow_3h) + " mm")

		# weather_description       varchar(20)
		try:
			description = data['weather'][0]['description']
		except Exception:
			print("API Call Error: No weather description.")
		else:
			# Save to database code here.
			insertWeatherDescription = "UPDATE weather_details " \
						"SET weather_description = '%s' WHERE date_calculated='%s' and city_name='%s';" % (description, dateCalculated, cityName)
			mycursor.execute(insertWeatherDescription)
			db.commit()
			print("Weather Description: \t" + str(description))

		# weather_icon				varchar(5)
		try:
			icon = data['weather'][0]['icon']
		except Exception:
			print("API Call Error: No weather icon.")
		else:
			# Save to database code here.
			insertWeatherIcon = "UPDATE weather_details " \
						"SET weather_icon = '%s' WHERE date_calculated='%s' and city_name='%s';" % (icon, dateCalculated, cityName)
			mycursor.execute(insertWeatherIcon)
			db.commit()
			print("Weather icon: \t\t\t" + str(icon))

		# weather_main				varchar(20)
		try:
			main = data['weather'][0]['main']
		except Exception:
			print("API Call Error: No weather main.")
		else:
			# Save to database code here.
			insertWeatherMain = "UPDATE weather_details " \
						"SET weather_main = '%s' WHERE date_calculated='%s' and city_name='%s';" % (main, dateCalculated, cityName)
			mycursor.execute(insertWeatherMain)
			db.commit()
			print("Weather Main: \t\t\t" + str(main))

		# city_ID					varchar(20)
		try:
			city_ID = data['id']
		except Exception:
			print("API Call Error: No city id.")
		else:
			# Save to database code here.
			insertWeatherMain = "UPDATE weather_details " \
						"SET city_ID = '%s' WHERE date_calculated='%s' and city_name='%s';" % (city_ID, dateCalculated, cityName)
			mycursor.execute(insertWeatherMain)
			db.commit()
			print("City ID: \t\t\t\t" + str(city_ID))


		# timezone		int
		try:
			timezone = data['timezone']
		except Exception:
			print("API Call Error: No timezone.")
		else:
			# Save to database code here.
			insertSunrise = "UPDATE weather_details " \
						"SET timezone = '%s' WHERE date_calculated='%s' and city_name='%s';" % (timezone, dateCalculated, cityName)
			mycursor.execute(insertSunrise)
			db.commit()
			print("Timezone: \t\t\t\t" + str(timezone))

		# latitude		float
		try:
			latitude = data['coord']['lat']
		except Exception:
			print("API Call Error: No latitude.")
		else:
			# Save to database code here.
			insertSunrise = "UPDATE weather_details " \
						"SET latitude = '%s' WHERE date_calculated='%s' and city_name='%s';" % (latitude, dateCalculated, cityName)
			mycursor.execute(insertSunrise)
			db.commit()
			print("Latitude: \t\t\t\t" + str(latitude))

		# longitude		float
		try:
			longitude = data['coord']['lon']
		except Exception:
			print("API Call Error: No longitude.")
		else:
			# Save to database code here.
			insertSunrise = "UPDATE weather_details " \
						"SET longitude = '%s' WHERE date_calculated='%s' and city_name='%s';" % (longitude, dateCalculated, cityName)
			mycursor.execute(insertSunrise)
			db.commit()
			print("Longitude: \t\t\t\t" + str(longitude))

		# sunrise		varchar(20)
		try:
			sunrise = data['sys']['sunrise']
		except Exception:
			print("API Call Error: No sunrise.")
		else:
			# Save to database code here.
			insertSunrise = "UPDATE weather_details " \
						"SET sunrise = '%s' WHERE date_calculated='%s' and city_name='%s';" % (sunrise, dateCalculated, cityName)
			mycursor.execute(insertSunrise)
			db.commit()
			print("Sunrise: \t\t\t\t" + str(sunrise))

		# sunset		varchar(20)
		try:
			sunset = data['sys']['sunset']
		except Exception:
			print("API Call Error: No sunset.")
		else:
			# Save to database code here.
			insertSunset = "UPDATE weather_details " \
						"SET sunset = '%s' WHERE date_calculated='%s' and city_name='%s';" % (sunset, dateCalculated, cityName)
			mycursor.execute(insertSunset)
			db.commit()
			print("Sunset: \t\t\t\t" + str(sunset))

		# country		varchar(30)
		try:
			country = data['sys']['country']
		except Exception:
			print("API Call Error: No country.")
		else:
			# Save to database code here.
			insertPressure = "UPDATE weather_details " \
						"SET country = '%s' WHERE date_calculated='%s' and city_name='%s';" % (country, dateCalculated, cityName)
			mycursor.execute(insertPressure)
			db.commit()
			print("Country: \t\t\t\t" + str(country))

		# main_pressure	int
		try:
			pressure = data['main']['pressure']
		except Exception:
			print("API Call Error: No pressure.")
		else:
			# Save to database code here.
			insertPressure = "UPDATE weather_details " \
						"SET main_pressure = '%s' WHERE date_calculated='%s' and city_name='%s';" % (pressure, dateCalculated, cityName)
			mycursor.execute(insertPressure)
			db.commit()
			print("Pressure: \t\t\t\t" + str(pressure))

		# grnd_level	int
		try:
			grnd_level = data['main']['grnd_level']
		except Exception:
			print("API Call Error: No grnd_level pressure.")
		else:
			# Save to database code here.
			insertGroundLevel = "UPDATE weather_details " \
						"SET grnd_level = '%s' WHERE date_calculated='%s' and city_name='%s';" % (grnd_level, dateCalculated, cityName)
			mycursor.execute(insertGroundLevel)
			db.commit()
			print("Ground level pressure: \t\t" + str(grnd_level))

		# sea_level	int
		try:
			sea_level = data['main']['sea_level']
		except Exception:
			print("API Call Error: No sea_level pressure.")
		else:
			# Save to database code here.
			insertSeaLevel = "UPDATE weather_details " \
						"SET sea_level = '%s' WHERE date_calculated='%s' and city_name='%s';" % (sea_level, dateCalculated, cityName)
			mycursor.execute(insertSeaLevel)
			db.commit()
			print("Sea level pressure: \t\t" + str(sea_level))

	# Else, print out error message, saying that user must wait for next weather update.
	elif 1 in rowExistsList[0]:
		print()
		print("Eh, no can do; date calculated already exists for \"" + cityName + "\". Try again later.")
		print("The latest update was at " + str(dateCalculated))

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