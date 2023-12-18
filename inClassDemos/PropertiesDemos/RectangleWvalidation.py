class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def set_size(self, size): # May only have one parameter besides self.
        if size[0] < 0 or size[1] < 0:
            raise Exception("Height and width must not be negative.")
        else:
            self.width = size[0]
            self.height = size[1]

    def get_size(self):
        return (self.width, self.height)

    size = property(get_size, set_size)

    def get_area(self):
        return self.width * self.height
    area = property(get_area) # Read only property

rectangle_one = Rectangle(10,20)
rectangle_one.size = (40,50) # Looks like an assignment but is actually a function call to set_size

print(f"The size of rectangle is: {rectangle_one.size} area is: {rectangle_one.area}") # Looks like accessing a variable, but is actually a function call to get_size through the property