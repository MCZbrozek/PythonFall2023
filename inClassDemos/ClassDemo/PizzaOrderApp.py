class PizzaOrder:
    # Set methods -> set in name, self + one attribute parameter, no return
    def set_Size(self, size):
        self.size = size

    # Get methods -> get in name, just self parameter, returns self . <attribute>
    def get_size(self):
        return self.size
    
    # Get and set for toppings
    def set_Toppings(self, toppings):
        self.toppings = toppings
        
    def get_toppings(self):
        return self.toppings
    
    # get price
    def get_price(self):
        if self.size == "small":
            price = 5
        elif self.size == "medium":
            price = 7
        else: 
            price = 9
        num_toppings = len(self.toppings)
        price = price + num_toppings * 1.00
        return price
    
pizza1 = PizzaOrder()
pizza1.set_Size("medium")
pizza1.set_Toppings(['cheese', 'anchovies', "pineapple"])
pizza2 = PizzaOrder()
pizza2.set_Size("large")
pizza2.set_Toppings(['pepperoni', 'garlic', 'basil', 'mushroom'])

print(pizza1.get_price())
print(pizza2.get_price())


