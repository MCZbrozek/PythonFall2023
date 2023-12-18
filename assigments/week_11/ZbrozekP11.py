"""ZbrozekP11
Programmer: Mike Zbrozek
Email: MZbrozek1@cnm.edu
Purpose: Create a user interface to load in a library of locations from .txt file. 
Allow user to input city and state to search for the closest point. 
Files associated with this assignment - ZbrozekP11.py, GeoPoint.py, TourList.py, P11Points.txt, gator.png"""

# tkinter
import tkinter as tk
import tkinter.scrolledtext as st

# PIL
from PIL import ImageTk, Image

# import requests for API call
import requests

# TourList class
from TourList import TourList

# GeoPoint class
from GeoPoint import GeoPoint

# https://www.geeksforgeeks.org/python-program-convert-string-list/
import ast

# ### Functions ###
###################################################
# Reads in text file, returns list of objects called pointList
def read_points_from_file(fileName):
    f = open(fileName, "r")
    line_num = 0
    tourList = TourList()
    while True:
        line = f.readline()
        if not line: break
        list = ast.literal_eval(line)
        tourList.coordList.append(list)
        line_num += 1
    f.close()
    return tourList

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

# Set the point objects created when the user reads in the file in the previous method
def set_point_objects(tourList, userLocation):
    pointList = []
    for loc in tourList.coordList:
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

# Function to print result for user
def format_result(closestLoc, userLocation):
    # Tell the user which point they are closest to.        
    result = f"Your favorite band will play in {(closestLoc.cityName)}, {(closestLoc.state)} which is {(closestLoc.distance)} miles away from {userLocation.cityName}, {userLocation.state}. "
    return result

# Method takes in the file path and loads the file
# I don't think that our file is persisting through when we click submit. We should try to call the read_points_from_file method and save that as list. That list should be able to be read in the submit method.  
def load():
    global tourList
    fileName = filename_entry.get()
    f = open(fileName, "r")
    tourList = read_points_from_file(fileName)
    contents_scrolled_text.delete("1.0", "end")
    contents_scrolled_text.insert("insert", tourList.coordList[0] + tourList.coordList[1])
    f.close
    

def submit():
    global userLocation
    userLocation = GeoPoint()
    userLocation.cityName = city_entry.get().title().strip()
    userLocation.state = state_entry.get().title().strip()
    api_result = get_from_api(userLocation)
    userLocation.point = location_details(api_result, userLocation)
    print(userLocation.point)
    pointList = set_point_objects(tourList, userLocation)
    closestLoc = closest_loc(pointList)
    result = format_result(closestLoc, userLocation)
    print(result)
    # Result
    contents_scrolled_text.delete("1.0", "end")
    contents_scrolled_text.insert("insert", result + "\n")
   

# ### GUI ###
###################################################

# Create the main window
top = tk.Tk()
top.title("Closest point")
contents_scrolled_text = st.ScrolledText()
contents_scrolled_text.grid(row = 6, column = 0,
       columnspan = 2, rowspan = 2, padx = 10, pady = 10,)

# File Name
filename_entry = tk.Entry()
filename_entry.grid(row=0,column=1, padx=10, pady=10, sticky= 'W')

filename_label = tk.Label(text="File Name to load coordinates")
filename_label.grid(row=0,column=0, padx=10, pady=10)

instructions_label = tk.Label(text="Enter the city and state where you are located:")
instructions_label.grid(row=2,column=0, columnspan= 3, padx=10, pady=10, sticky='W')

# City Name
city_entry = tk.Entry()
city_entry.grid(row=3,column=1, padx=10, pady=10, sticky= 'W')

city_label = tk.Label(text="Enter City")
city_label.grid(row=3,column=0, padx=10, pady=10)

# State Name
state_entry = tk.Entry()
state_entry.grid(row=4,column=1, padx=10, pady=10, sticky= 'W')

state_label = tk.Label(text="Enter State (full state name only)")
state_label.grid(row=4,column=0, padx=10, pady=10)

# Open button
tk.Button(text="Open File", command=load, bg="lightgreen").grid(row=1,column=1, padx=0, pady=5, sticky= 'W')

# Submit button
tk.Button(text="Submit", command=submit, bg="lightblue").grid(row=5,column=1, padx=0, pady=5, sticky= 'W')

#  Create an object of tkinter ImageTk 
# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/
image = Image.open("gator.png")
resize_image = image.resize((150, 150))
test = ImageTk.PhotoImage(resize_image)
label1 = tk.Label(image=test)
label1.image = test
label1.grid(row=5,column=2, padx=5, pady=5, sticky= 'W')

# Mainloop
tk.mainloop()