class Computer:
    def __init__ (self, serial_number = "unknown" ,make = "unknown",model = "unknown",person = "unassigned"):
        self.serial_number = serial_number
        self.make = make
        self.model = model
        self.person = person

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number
    def get_serial_number(self):
        return self.serial_number

    def set_make(self, make):
        self.make = make
    def get_make(self):
        return self.make

    def set_model(self, model):
        self.model = model
    def get_model(self):
        return self.model

    def set_person(self, person):
        self.person = person
    def get_person(self):
        return self.person    
    
computer1 = Computer()
print(f" Make = {computer1.get_make()}, Model= {computer1.get_model()}, Person = {computer1.get_person()}, serial Number = {computer1.get_serial_number()}")

# Computer arrives at the loading doc, add the serial number 1234-5678, dell for make, model inspirion 

computer2 = Computer(serial_number="1234-5678", make="Dell", model="Inspirion")

print(f" Make = {computer2.get_make()}, Model= {computer2.get_model()}, Person = {computer2.get_person()}, serial Number = {computer2.get_serial_number()}")
