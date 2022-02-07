# Description of Program

This program is a Windows service that will automatically call and store weather data at a user defined time.

# Planned Automation Features

- Start automatically on startup, without input.
- Work in the background, without user input.
- Let user choose weather data location(s).
- Let user choose weather data retrieval time.
- Let user choose weather data retrieval frequency.
- Store this data into a local MySQL relationsal database at each API call.

# Installation Instructions for Development

1. Clone github repository to local computer.
2. Open Pycharm
3. Configure an interpreter; this makes the virtual environment that you need.
4. Install all pip packages from requirements.txt in the virtual environment. Use "pip install -r requirements.txt" command.
5. Copy necessary files into the project folder that aren't pip dependencies (in this case, .env).
6. Add a python run configuration for the .py file, main. This lets you run that python file.
