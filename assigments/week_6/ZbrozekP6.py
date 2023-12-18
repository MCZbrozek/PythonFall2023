# ZbrozekP6
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose:Calculate the distance between to geographic points.
#  test coords Abq and Denver
# Expected output = 535.293km convert to miles 332.615
# abq = (35.106766, -106.629181)
# den = (39.742043, -104.991531)

# import operators from math
from math import sin, cos, sqrt, pi, atan2, asin, radians

# --- Function Definitions ---
# header will print summary explaining the purpose of the program
def header():
    print("The Haversine formula calculates the shortest distance between two points on a sphere. Enter the Lat and long for two locations to see how far they are apart.\n  ")
    print("Enter the details of your first location below -\n")
    
# Asks the user for the latitude and the longitude, returns a tuple or list with the lat/long. In decimal degrees
def get_location():
    lat = float(input("Enter the Latitude in Decimal degress: "))
    long = float(input("Enter the Longitude in Decimal degress: "))
    coord = (lat, long)
    return coord

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

# --- Run Program ---
while True:
    header()
    coord1 = get_location()
    print("\nEnter the details of your second location below -\n ")
    coord2 = get_location()
    dist = distance(coord1, coord2)
    dist_miles = convert_to_miles(dist)
    print(f"The distance between the two locations is {dist} km or {dist_miles} miles ")
    runAgain = input("Enter (Q) to quit or 'Y to calculate another distance.")
    if runAgain.lower() == 'q': break 