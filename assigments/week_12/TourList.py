"""ZbrozekP11
Programmer: Mike Zbrozek
Email: MZbrozek1@cnm.edu
Purpose: Create a user interface to load in a library of locations from .txt file. 
Allow user to input city and state to search for the closest point. 
Files associated with this assignment - ZbrozekP11.py, GeoPoint.py, TourList.py, P11Points.txt, gator.png"""

class TourList:
    def __init__(self, data=[]):
        self.__data = data

    def set_data(self, list):
        self.__data = list
    def get_data(self):
        return (self.__data)
    
    coordList = property(get_data, set_data)
