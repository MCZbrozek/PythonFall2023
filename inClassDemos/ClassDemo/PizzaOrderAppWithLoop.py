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
pizzas = []    
do_another = "y"
while do_another == "y":
    size = input("Please enter 'Small', 'medium' or 'large' for size: ")
    # Get toppings from user
    toppings = []
    while True:
        topping = input("Add your toppings and press enter. When finished press enter: ")
        if not topping: break
        toppings.append(topping)
    # create a PizzaOrder Object get values and set price
    pizza = PizzaOrder()
    pizza.set_Size(size)
    pizza.set_Toppings(toppings)
    price = pizza.get_price()
    pizzas.append(pizza)
    print(f"The price of this pizza is")

    do_another = input('Do another (y/n)? ')

print(pizzas)
print("Your pizzas: ")
for pizza in pizzas:
    print(pizza.get_size(), pizza.get_toppings(), pizza.get_price())
