# ZbrozekP9
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose: Create a better class and load in a library of locations from .txt file
#Files associated with this assignment - ZbrozekP9.py, GeoPoint.py

class GeoPoint:
    def __init__(self, lat = 0, lon = 0, city = "defaultCity", state = "defaultState", description = "DefaultDescription"):
        self.__lat = lat
        self.__lon = lon
        self.__city = city
        self.__state = state
        self.__description = description

    def set_point(self, point):
        self.__lat = point[0]
        self.__lon = point[1]
    def get_point(self):
        return (self.__lat, self.__lon)
    
    point = property(get_point, set_point)
        
    def set_city(self, city):
        self.__city = city
    def get_city(self):
        return self.__city
    
    cityName = property(get_city,set_city)
    
    def set_state(self, state):
        self.__state = state
    def get_state(self):
        return self.__state
    
    state = property(get_state, set_state)

    def set_description(self, description):
        self.__description = description
    def get_description(self):
        return self.__description
    
    desc = property(get_description, set_description)