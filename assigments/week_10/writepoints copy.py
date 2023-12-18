# https://www.geeksforgeeks.org/python-program-convert-string-list/
import ast

from GeoPoint import GeoPoint

userLocation = GeoPoint(35.106766, -106.629181, "Albuquerque", "New Mexico", "a magical place")

file = open("P10Points.txt","w")
locs = [["36.111031", "-115.172821", "Las Vegas", "Nevada", "Bakkt Theater at Planet Hollywood"],["33.448502", "-112.079292", "Phoenix", "Arizona", "Arizona Financial Theatre"], ["35.134690", "-106.615970","Albuquerque", "New Mexico", "Revel Entertainment Center"], ["35.466091", "-97.504303", "Oklahoma City", "Oklahoma", "The Criterion"],["36.1172783", "-94.157178", "Fayetteville", "Arkansas", "JJ's Live"], ["30.134165", "-97.638428", "Austin", "Texas", "Germania Insurance Ampitheater"]]

for list in locs:
    file.write("%s\n" % list)
    # for string in list:
    #  file.write(str(string))   
file.close()    

# Reads in text file, returns list of objects called pointList
# Change this for new files, text should be formatted - 
# [["36.111031", "-115.172821", "Las Vegas", "Nevada", "Bakkt Theater at Planet Hollywood"],["33.448502", "-112.079292", "Phoenix", "Arizona", "Arizona Financial Theatre"]]
fileLocation = "P10Points.txt"
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



# Loop through the list of points, run the distance and convert to miles formula return the geoPoint from the list that is closest to the user 
# def closestTourLocation(userLocation, pointList):
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


pointList = create_points_from_file(fileLocation)
closestLoc = closest_loc(pointList)
print(closestLoc.cityName, closestLoc.distance)