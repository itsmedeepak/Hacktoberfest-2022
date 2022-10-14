import subprocess,sys
def install(package):
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])

install("requests")



print ("see the output in potrait view\n\n")

import requests , json
import pandas as pd
import datetime

a = [57, 54, 101, 100, 54, 57, 55, 55, 101, 56, 102, 98, 56, 53, 99, 55, 55, 57, 97, 52, 101, 51, 97, 101, 50, 100, 101, 56, 50, 52, 102, 101]
st = ""
for i in a:
    st+=chr(i)

user_api = st
location = input() or "chunar"

complete_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_link)
api_data = api_link.json()

def decor(x):
    return "    —"+" "*5 + str(x) + " "*(22 - len(str(x)))+"|"

if api_data["cod"] == "404":
    print("invalid")
else :
    print(f"{location:-^53}")
    data = {
        "":[
            decor(str(api_data["coord"]['lat'])+" °"), 
            decor(str(api_data["coord"]['lon'])+" °"),
            decor(api_data["weather"][0]["description"]),
            decor(str(round(api_data["main"]["temp"]-273,2))+" °C"),
            decor(str(round(api_data["main"]["feels_like"]-273,2))+" °C"),
            decor(str(round(api_data["main"]["temp_min"]-273,2))+" °C"),
            decor(str(round(api_data["main"]["temp_max"]-273,2))+" °C"),
            decor(str(api_data["main"]["pressure"])+" millibars"),
            decor(str(api_data["main"]["humidity"])+" %"),
            decor(str(api_data["visibility"])+" m"),
            decor(str(api_data["wind"]["speed"])+" m/s"),
            decor(str(api_data["wind"]["deg"])+" °"),
            decor(datetime.datetime.fromtimestamp(api_data["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M:%S')),
            decor(datetime.datetime.fromtimestamp(api_data["sys"]["sunset"]).strftime('%Y-%m-%d %H:%M:%S')),
            decor(api_data["sys"]["country"]),
            decor(api_data["timezone"])
            ]
    }
    a = pd.DataFrame(data,index=[
        "Latitude", 
        "longitude",
        "Weather",
        "Average Temprature",
        "Feels Like",
        "Minimum Temprature",
        "Maximum Temprature",
        "Average Pressure",
        "Average Humidity",
        "area visibility",
        "wind speed",
        "wind direction",
        "sun rise",
        "sun set",
        "country",
        "time zone"
        ])
    print(a)
