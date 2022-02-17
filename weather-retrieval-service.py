import time
import random
from pathlib import Path
from SMWinservice import SMWinservice
import mysql.connector      # Used to run SQL commands in Python
import requests             # Used to call the HTTP API.
from dotenv import load_dotenv      # Used to store the API key
import os                   # Used to access environmental variables, and my API key.
import pprint               # Simply prints out .json output in a much neater format.
import datetime
import sys
import weather_retrieval_tool

class PythonCornerExample(SMWinservice):
    _svc_name_ = "PythonCornerExample"
    _svc_display_name_ = "Python Corner's Winservice Example"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        print("Hey, listen!")
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

        # dotenv, for environment variables and protection of API key.
        load_dotenv()

        # Instead of making GUI now, focus command line interface.

        while True:
            userCommand = input("Enter a command: ")
            userInput(userCommand)


if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
