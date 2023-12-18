import requests
from operator import itemgetter

city = input("Please enter a city name: ").lower()
state = input("Please enter a state name: ").lower()

# city = 'albuquerque'
# state = 'new mexico'
api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&state={}'.format(city, state)
response = requests.get(api_url + city, headers={'X-Api-Key': 'TZ0VP0KSap3UlLk8LNTPvQ==ijVzHGbhMVfketRi'})
if response.status_code == requests.codes.ok:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)
    print("Else Block")

loc_details = data[0]

def location_details(loc_details):
    lat = loc_details["latitude"]
    lon = loc_details["longitude"]
    coords = (lat, lon)
    return coords

test = list(map(itemgetter('name'), data))


print("Our list of strings is: " + str(loc_details))
coords = location_details(loc_details)
print(f"The coordinates for '{city}', '{state}' are {coords}")
