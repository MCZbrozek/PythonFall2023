class PizzaOrder:
    def __init__(self, size = "medium", toppings = ['cheese']):
        self.__size = size # __size basically makes this variable private, and forces a user to have to use the get and set methods (and their validation) to set them. 
        self.__toppings = toppings

    def set_size(self, size):
        self.__size = size
    def get_size(self):
        return self.__size
    
    size = property(get_size, set_size)
    
    def set_toppings(self, toppings):
        self.__toppings.toppings
    def get_toppings(self):
        return self.__toppings
    
    toppings = property(get_size, set_size)

    def get_price(self):
        if self.__size == "small":
            price = 5.0
        elif self.__size == "medium":
            price = 7.0
        else:
            price = 9.0
        num_toppings = len(self.__toppings)
        price += num_toppings*1.25
        return price
    price = property(get_price) # Read only property

