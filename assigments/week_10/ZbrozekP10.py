# ZbrozekP10
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose: Create a better class and load in a library of locations from .txt file
#Files associated with this assignment - ZbrozekP10.py, P10Points.txt, GeoPoint.py

# import GeoPoint class
from GeoPoint import GeoPoint

# import writepoints to create txt file if it does't exist
from writepoints import writeFile

# import operators from math
from math import sin, cos, sqrt, pi, atan2, asin, radians

# import requests for API call
import requests

# https://www.geeksforgeeks.org/python-program-convert-string-list/
import ast

# Change this for new files, text should be formatted - 
fileLocation = "P10Points.txt"

# ^^^^ FUNCTION DEFINITIONS ^^^^
# header will print summary explaining the purpose of the program
def header():
    print("\nYour favorite band, KING GIZZARD AND THE LIZARD WIZARD, is on tour! Some tour locations are listed in a .txt file, enter your city and state to see which venue you are closest to.\n  ")

# Asks the user for the latitude and the longitude, returns a tuple with the lat/long. In decimal degrees
def get_location_from_user():
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

# Reads in text file, returns list of objects called pointList
def create_points_from_file(fileLocation):
    f = open(fileLocation, "r")
    line_num = 0
    tourList = []
    while True:
        line = f.readline()
        if not line: break
        list = ast.literal_eval(line)
        tourList.append(list)
        line_num += 1

    f.close()
    
    pointList = []
    for loc in tourList:
        newPoint = GeoPoint(
            float(loc[0]),
            float(loc[1]),
            loc[2],
            loc[3],
            loc[4],        
            )
        newPoint.set_distance(userLocation)
        pointList.append(newPoint)
    return pointList

# Loop through the list of points, run set the distance attribute on the newPoint object and convert to miles formula.  
# Return the geoPoint from the list that is closest to the user 

def closest_loc(pointList):
    relDistance = pointList[0].distance
    closestLoc = None
    for point in pointList:
        dist = point.distance
        if dist <= relDistance:
            relDistance = dist
            closestLoc = point
        else:
            relDistance = relDistance
    return closestLoc

# --- RUN PROGRAM ---
# Write text file
writeFile(fileLocation)

while True:
    header()
    
    try:
        # Ask user for their location
        userLocation = get_location_from_user()

        # retrieve the information from the API using the userLocation
        api_result = get_from_api(userLocation)
        userLocation.point = location_details(api_result, userLocation)

        # run methods to return closestLoc object
        pointList = create_points_from_file(fileLocation)
        closestLoc = closest_loc(pointList)
        
        # Tell the user which point they are closest to.        
        print(f"Your favorite band will is play in {(closestLoc.cityName)}, {(closestLoc.state)} which is {(closestLoc.distance)} miles away from {userLocation.cityName}, {userLocation.state}. ")
        
        runAgain = input("Enter (Q) to quit or (Y) to calculate another distance: ")
        
        if runAgain.lower() == 'q': 
            print("\nWe hope you learned something! Thank you!")
            break

    except (IndexError, KeyError):
        print("Entry not accepted, please type a City and State name. ")
    except (UnboundLocalError):
        print("Unfortunately your request timed out, or you are not connected to the internet. Please check your connection and try again.")
    

     
