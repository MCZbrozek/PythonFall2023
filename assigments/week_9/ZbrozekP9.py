# ZbrozekP9
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose: Create a better class and load in a library of locations from .txt file
#Files associated with this assignment - ZbrozekP9.py, GeoPoint.py

# import GeoPoint class
from GeoPoint import GeoPoint

# import operators from math
from math import sin, cos, sqrt, pi, atan2, asin, radians

# import requests for API call
import requests

# ^^^^ FUNCTION DEFINITIONS ^^^^
# header will print summary explaining the purpose of the program
def header():
    print("\nEnter your City and State to find out if you are closer to Albany or Albuquerque\n  ")

# Asks the user for the latitude and the longitude, returns a tuple with the lat/long. In decimal degrees
def get_location():
    userLocation = GeoPoint()
    print("Enter the city and state where you are located -")
    userLocation.cityName = input("Please enter a city name: ").title().strip()
    if not isinstance(userLocation.cityName, str):
        raise TypeError("There aren't numbers in a city name.")
    userLocation.state = input("Please enter a state name: ").title().strip()
    return userLocation

# Makes request from api-ninjas API 
# https://api-ninjas.com/api/geocode
def get_from_api(userLocation):
    city = userLocation.cityName
    state = userLocation.state
    api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&state={}'.format(city, state)
    try:
        response = requests.get(api_url + city + state, headers={'X-Api-Key': 'TZ0VP0KSap3UlLk8LNTPvQ==ijVzHGbhMVfketRi'}, timeout = 1)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errHttp:
        print("Http Error")
        print(errHttp.args[0])
    except requests.exceptions.ReadTimeout as errTime:
        print("The request has Timed Out.")
    except requests.exceptions.ConnectionError as connectionError:
        print("Check your connection and try again!")
    except requests.exceptions.RequestException as errGeneral:
        print("Hmmm, something didn't work quite right. Try your entry again.")
    data = response.json()
    return data

# Pulls the lat/long details from the API results assigns them to the userLocation Object
def location_details(api_result, userLocation):
    i = 0
    loc_details = None
    for res in api_result:
        res = res.get('state').title()
        if res == userLocation.state:
            loc_details = api_result[i]
        i = i + 1
    lat = float(loc_details["latitude"])
    lon = float(loc_details["longitude"])
    coords = (lat, lon)
    return coords
    
# Takes two tuples (lat,long) calcs distance between 2 geographic points using Haversine formula
def distance(coord1, coord2):

    radius = 6371 # KM

    # distance between lats and longs converted to radians
    dlat = radians(coord2[0] - coord1[0])
    dlong = radians(coord2[1] - coord1[1])

    # Lats converted to radians
    lat1 = radians(coord1[0])
    lat2 = radians(coord2[0]) 

    # apply Haversine formula
    a = pow(sin(dlat / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(dlong / 2), 2)

    c = 2 * atan2(sqrt(a), sqrt(1-a))
    # c = 2 * asin(sqrt(a))
    return round(radius * c,3)

# convert result of "distance" to miles
def convert_to_miles(dist):
    dist_miles = round(dist * 0.621371, 2)
    return dist_miles

# Instantiate two points use SetPoint and SetDescription methods make sure they have unique coordinates and descriptions

albuquerque = GeoPoint(35.106766, -106.629181, "Albuquerque", "New Mexico", "a magical place" )
# albuquerque.city = "Albuquerque"
# albuquerque.state = "New Mexico"
# albuquerque.point = ((35.106766, -106.629181))
# albuquerque.desc = ("a magical place")

albany = GeoPoint()
albany.cityName = "Albany"
albany.state = "New York"
albany.point = ((42.65258, -73.75623))
albany.desc = ("the capital of New York")

# --- RUN PROGRAM ---
while True:
    header()
    
    try:
        # Ask user for their location
        userLocation = get_location()

        # retrieve the information from the API using the userLocation
        api_result = get_from_api(userLocation)
        userLocation.point = location_details(api_result, userLocation)
        # Use point 1 and point2's distance method to find the distance from each point to the user's location
        dist1 = convert_to_miles(distance(albuquerque.point, userLocation.point))
        dist2 = convert_to_miles(distance(albany.point, userLocation.point))

        # Tell the user which point they are closest to.
        if dist1 < dist2:
            print(f"Your location, {(userLocation.cityName)} is closest to {albuquerque.cityName}, {albuquerque.desc}. You are only {dist1} miles away.")
        else:
            print(f"Your location, {userLocation.cityName} is closest to {albany.cityName}, {albany.desc}. You are only {dist2} miles away.")
        
        runAgain = input("Enter (Q) to quit or (Y) to calculate another distance: ")
        
        if runAgain.lower() == 'q': 
            print("\nWe hope you learned something! Thank you!")
            break

    except (IndexError, KeyError):
        print("Entry not accepted, please type a City and State name. ")
    except (UnboundLocalError):
        print("Unfortunately your request timed out, or you are not connected to the internet. Please check your connection and try again.")
    

     
