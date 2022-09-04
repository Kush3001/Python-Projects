import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

data = requests.get(
    "https://newsapi.org/v2/top-headlines?country=in&apiKey=4e6d3e85500e49a581b30d0ee64bf578")
result = data.json()
news = result['articles']
speak("Daily News Updates")
for i in range(0,2):
    speak(f"News - {i+1}")
    speak(news[i]["title"].split("-")[0])
speak("That is the end of Today's News. Thank You")