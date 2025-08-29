import json
import re
from tkinter.font import names

import requests

# Load the corrected JSON
with open(r"/Users/elkbusinesshub/Downloads/city.list.json", "r", encoding="utf-8") as f:
    city_data = json.load(f)
#print(city_data[])
user_req = input("What's your query? ")
# print(user_req.lower())
user_req_list = user_req.split(' ')
# print(user_req_list)

for cities in city_data:
    if(cities['name'].lower() in user_req_list):
        city_found = cities['name']
        # break
print("Detected cities:", city_found)

def get_weather(city_found):
    API_KEY = "a5356df3b9e444022efcb87cc8bd4c73"  # Use consistent variable name
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_found}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"Weather in {city_found}: {temp}°C, {desc}")
    else:
        print(f"Could not get weather data for {city_found}")


get_weather(city_found)
