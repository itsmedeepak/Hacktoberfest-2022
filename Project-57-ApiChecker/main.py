import requests

ip = requests.get('https://ipinfo.io/json').json()['ip']

print('your ip is: ', ip)