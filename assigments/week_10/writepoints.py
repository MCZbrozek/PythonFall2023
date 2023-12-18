import os.path

def writeFile(fileLocation):
    if not os.path.isfile(fileLocation):
        file = open("P10Points.txt","w")
        locs = [["36.111031", "-115.172821", "Las Vegas", "Nevada", "Bakkt Theater at Planet Hollywood"],["33.448502", "-112.079292", "Phoenix", "Arizona", "Arizona Financial Theatre"], ["35.134690", "-106.615970","Albuquerque", "New Mexico", "Revel Entertainment Center"], ["35.466091", "-97.504303", "Oklahoma City", "Oklahoma", "The Criterion"],["36.1172783", "-94.157178", "Fayetteville", "Arkansas", "JJ's Live"], ["30.134165", "-97.638428", "Austin", "Texas", "Germania Insurance Ampitheater"]]

        for list in locs:
            file.write("%s\n" % list)
            # for string in list:
            #  file.write(str(string))   
        file.close()    

