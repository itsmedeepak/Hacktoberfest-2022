import requests
import os
from twilio.rest import Client

API_KEY = "PLEASE_INSERT_WEATHER_API"
END_POINT = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = 'PLEASE_INSERT_AUTH_KEY'
auth_token = 'PLEASE_INSERT_AUTH_KEY'


def send_sms():
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=" \n It is going to rain today !, Remember to bring umbrella 😎.\n\n\nThanks and Regards\nDeepak Kumar.",
        from_='+19124726193',
        to='+918804375275'
    )

    print(message.sid)


parameter = {
    "lat": 24.7914,
    "lon": 85.0002,
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": API_KEY,

}

response = requests.get(END_POINT, params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) > 700:
        send_sms()
        break
