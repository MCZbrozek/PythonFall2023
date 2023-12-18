from unicodedata import normalize

class BuildingPermit:
    def __init__(self,type="residential",date="19710101"):
        self.type = type
        self.date = date

    def get_type(self):
        return self.__type
    def set_type(self,type):
        self.__type = type
    type = property(get_type, set_type)

    def get_date(self):
        return self.__date
    def set_date(self,date):
        self.__date = date
    date = property(get_date, set_date)

#open the file
f = open("BuildingPermitsCABQ-en-us.csv", 'r', encoding="unicode-escape")

#read the file into a data structure
data = []
f.readline() #Discards the header row

while True:
    line = f.readline()
    if not line: break
    elements = line.split('\t')
    bp = BuildingPermit()
    bp.type = elements[1]
    bp.date = elements[15]
    data.append(bp)

# print(data)
#print(data[3][2]) # Gives me the row and the column
# print(line)
num_residential_permits_in_2023 = 0
#find number of residential permits in 2023
for permit in data:
    if permit.date.startswith('2023'):
        if permit.type == 'Residential':
            num_residential_permits_in_2023 += 1 # Counts the amount of permits that meet criteria 
print(f"There were {num_residential_permits_in_2023} permits in 2023")
#close the file
f.close()