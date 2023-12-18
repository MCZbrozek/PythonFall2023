# ZbrozekP10
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose: Create a better class and load in a library of locations from .txt file
#Files associated with this assignment - ZbrozekP10.py, GeoPoint.py

from math import sin, cos, sqrt, pi, atan2, asin, radians


class GeoPoint:
    def __init__(self, lat = 0, lon = 0, city = "defaultCity", state = "defaultState", description = "DefaultDescription", distance = 0):
        self.__lat = lat
        self.__lon = lon
        self.__city = city
        self.__state = state
        self.__description = description
        self.__distance = distance

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

    # Takes two tuples (lat,long) calcs distance between # 2 geographic points using Haversine formula
    # def distance(coord1, coord2):
    def set_distance(self, userLocation):
        radius = 6371 # KM
        coord1 = self.point
        coord2 = userLocation.point
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
        distance = round(radius * c,3)
        distance = round(distance * 0.621371, 2)
        self.__distance = distance
    
    def get_distance(self):
        return self.__distance
    
    
    distance = property(get_distance, set_distance)


