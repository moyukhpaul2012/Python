import requests
import json
import pyttsx3 # pip install pyttsx3

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=API_KEY={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()