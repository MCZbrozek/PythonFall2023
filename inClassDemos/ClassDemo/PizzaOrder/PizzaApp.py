import PizzaOrder

def header():
    print("Welcome to Python Pizza.")
    print()

def say_goodbye():
    print("Thank you for your order!")
    print("Goodbye!! ")

def pizza_size():
    size = input("How big is this Pizza (Small, Medium, Large)? ")
    return size

def pizza_toppings():
    toppings = []
    while True:
        topping = input("Please enter a topping or enter to quit: ")
        if not topping: break
        toppings.append(topping)
    return toppings

if __name__ == "__main__":
        # Display a header
    header()

    # Do another
    do_another = 'y'

    while do_another == 'y':


        # Get a size from user
        
        size = pizza_size()
        # Gets toppings from user
        toppings = pizza_toppings()

        # Instanciate Pizza objects 
        pizza = PizzaOrder(size, toppings)

        # Display pizza
        print(f"Your pizza is size {pizza.size}, {pizza.toppings}")

        # Then displays a price
        print(f"Your pizza's price is {pizza.price}")

        do_another = input("Do another pizza (y/n): ").lower()

        # Says GoodBye
    say_goodbye()