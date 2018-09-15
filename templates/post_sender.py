import requests
import json

# Ton to be sent
drone_data = '{ "icao": "FA4548", "lat": 46.530834474, "lon": 6.2578792135, "alt": 9753, "speed": 236.129796, "heading": -51.76, "last_update": "2018-09-14T22:42:25.898475+00:00" }'

url = "http://0.0.0.0:3000/post_drone_position"

files = [
    ('drone_json', ('drone_json', json.dumps(drone_data), 'application/json')),
]

r = requests.post(url, files=files)
print(str(r.content, 'utf-8'))