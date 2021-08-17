import requests
import os
from twilio.rest import Client

API_KEY = "33234c0b48ef3c48449d0da2e72c566a"
END_POINT = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = 'AC7c30f5ed181b22f7918315cc7d731c8e'
auth_token = '60cc4554667a0e2905c0742e9f5544d2'


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
