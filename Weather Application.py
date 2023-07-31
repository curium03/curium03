import requests
import json
import pyttsx3

def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=3a0d31783955468b8be62013231007&q={city}"
r = requests.get(url)
WDict = json.loads(r.text)

weather = WDict["current"]["condition"]["text"]
temperature = WDict["current"]["temp_c"]

text = f"The current weather in {city} is {weather}. The temperature is {temperature} degrees Celsius."
text_to_speech(text)
