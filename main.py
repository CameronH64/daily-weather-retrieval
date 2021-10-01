import requests             # Used to call the HTTP API.
from dotenv import load_dotenv      # Used to store the API key
import os                   # Used to access environmental variables, and my API key.
import pprint               # Simply prints out .json output in a much neater format.
import mysql.connector      # Used to run SQL commands in Python
from tkinter import *
from PIL import ImageTk, Image
import datetime

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

# Plain OpenWeatherMap API calls
# https:/api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
OWMCity = "http:/api.openweathermap.org/data/2.5/weather?q={}&appid={}"
# https:/api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}
OWMCityID = "http:/api.openweathermap.org/data/2.5/weather?id={}&appid={}"
# https:/api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
OWMCoordinates = "http:/api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
# https:/api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}
OWMZipCode = "http:/api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}"

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

root = Tk()
root.geometry("800x400")

def searchButtonClicked():
    return searchEntry.get()

######################### CREATE ELEMENTS FOR GUI #########################

# LABEL for search parameters
question = Label(root, text="Enter your search parameters: ")
question.grid(row=0, column=0)

# ENTRY textbox for search parameters
searchEntry = Entry(root, width=40)
searchEntry.grid(row=1, column=0)

# BUTTON for submit
submissionButton = Button(root, text="Search", command=lambda: searchButtonClicked())
submissionButton.grid(row=1, column=1)

# LABEL widget for API call return
output = Label(root, wraplength=500)
output.grid(row=2, column=0)

#======================== END CREATE ELEMENTS FOR GUI ============

# returnedData = OWMCall("City")
# pprint.pprint(returnedData)

# Activate the mainloop window
root.mainloop()

APICall = requests.get("http:/api.openweathermap.org/data/2.5/weather?q=conway&appid=3f50437fe51d585ab8a11be93c75efc3")
data = APICall.json()
pprint.pprint(data)

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