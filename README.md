# Description of Program

This program will have a simple, intuitive GUI that will search for the current weather in user-specified locations. This program will also be able to save that weather data into a local MySQL database.

There are plans to make this an optionally automated program to store weather data as time passes. This feature will be implemented once the main program is complete.

# Main GUI Program Features

- A basic, but intuitive and robust GUI.
- Let user choose specific parameters to search and record weather data from.
- Store a weather API call in a relational database.

# Planned Program Automation Features

- Start automatically on computer startup, without user interference.
- Work in the background, without user interference.
- Let user choose weather data location(s).
- Let user choose weather data retrieval time.
- Let user choose weather data retrieval frequency.
- Store this data reliably into a local MySQL relationsal database at each API call.

# Installation Instructions for Development

1. Clone github repository to local computer.
2. Open Pycharm
3. Configure an interpreter; this makes the virtual environment that you need.
4. Install all pip packages from requirements.txt in the virtual environment. Use "pip install -r requirements.txt" command.
5. Copy necessary files into the project folder that aren't pip dependencies (in this case, .env).
6. Add a python run configuration for the .py file, main. This lets you run that python file.
