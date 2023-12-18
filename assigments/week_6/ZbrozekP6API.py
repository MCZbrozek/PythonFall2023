# ZbrozekP6
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose:Calculate the distance between to geographic points called from API


# import operators from math
from math import sin, cos, sqrt, pi, atan2, asin, radians

# import requests for API call
import requests

# --- FUNCTION DEFINITIONS ---
# header will print summary explaining the purpose of the program
def header():
    print("The Haversine formula calculates the shortest distance between two points on a sphere. Enter the CITY and STATE for two locations to see how far they are apart.\n  ")
    print("Enter the details of your first location below -\n")
    
# Asks the user for the latitude and the longitude, returns a tuple with the lat/long. In decimal degrees
userLoc = {"city" : "", "state" : "" }
def get_location(userLoc):
    print("Enter a city and state you'd like to know the distance between -")
    userLoc["city"] = input("Please enter a city name: ").lower()
    userLoc["state"] = input("Please enter a state name: ").lower()
    return userLoc

# Makes request from api-ninjas API 
# https://api-ninjas.com/api/geocode
def get_from_api(userLoc):
    city = userLoc["city"]
    state = userLoc["state"]
    api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&state={}'.format(city, state)
    response = requests.get(api_url + city, headers={'X-Api-Key': 'TZ0VP0KSap3UlLk8LNTPvQ==ijVzHGbhMVfketRi'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code, response.text)
    

# Pulls the lat/long details from the API results
def location_details(api_result):
    loc_details = api_result[0]
    lat = float(loc_details["latitude"])
    lon = float(loc_details["longitude"])
    coords = (lat, lon)
    return coords
    
#  Runs a loop to get location from user, and check that the city and state are correct before proceeding 
def nextloc(userLoc):
    while True:
        userLoc = get_location(userLoc)
        api_result = get_from_api(userLoc)
        userLoc["coordinates"] = location_details(api_result)
        print(f"The coordinates for '{userLoc['city']}', '{userLoc['state']}' are {userLoc['coordinates']} - ")
        nextLoc = input("Does this look right? (C)ontinue or (S)earch again: ")
        if nextLoc.lower() == 'c': break
    return userLoc


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

def convert_to_miles(dist):
    dist_miles = round(dist * 0.621371, 3)
    return dist_miles

# --- RUN PROGRAM ---
while True:
    header()
    # Get First location
    userLoc1 = nextloc(userLoc)
    coord1 = userLoc1['coordinates']
    city1 = userLoc1['city'].title()
    # Get Second location
    print("\nEnter the details of your second location below -\n ")
    userLoc2 = nextloc(userLoc)
    coord2 = userLoc2['coordinates'] 
    city2 = userLoc2['city'].title()
    
    # Run Haversine calculation
    dist = distance(coord1, coord2)
    # Convert result to miles
    dist_miles = convert_to_miles(dist)
    # Display result to user
    print(f"The distance between {city1} and {city2} is {dist} km or {dist_miles} miles. \n ")

    runAgain = input("Enter (Q) to quit or 'Y to calculate another distance.")
    if runAgain.lower() == 'q': break 