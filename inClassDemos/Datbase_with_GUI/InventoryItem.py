class InventoryItem:
    def __init__(self, row_id = 0, serial_number = 0, description = "", location = "loading dock", date_arrived = "", date_left = ""):
        self.__row_id = row_id
        self.__serial_number = serial_number
        self.__description = description
        self.__location = location
        self.__date_arrived = date_arrived
        self.__date_left = date_left

    def get_row_id (self):
        return self.__row_id
    def set_row_id (self,row_id):
        self.__row_id = row_id 
    row_id =property(get_row_id,set_row_id)
  
    def get_serial_number (self):
        return self.__serial_number
    def set_serial_number (self,serial_number):
        self.__serial_number = serial_number 
    serial_number =property(get_serial_number,set_serial_number)

    def get_description (self):
        return self.__description
    def set_description (self,description ):
        self.__description = description
    description=property(get_description, set_description)

    def get_location (self):
        return self.__location
    def set_location (self,location ):
        self.__location = location
    location=property(get_location, set_location)

    def get_date_arrived (self):
        return self.__date_arrived
    def set_date_arrived (self,date_arrived ):
        self.__date_arrived = date_arrived
    date_arrived=property(get_date_arrived, set_date_arrived)

    def __str__(self):
        return f'{self.row_id}: {self.__description} serial: {self.serial_number} located at: {self.location}'

    