import requests
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

APIKey = os.getenv("API_KEY")

cityName = input("Enter a city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIKey}"

result = requests.get(url)

data = result.json()

pprint.pprint(data)

