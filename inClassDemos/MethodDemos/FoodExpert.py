class FoodExpert:
    def __init__(self):
        self.good_Food = []
        self.name = "unkown"
    
    def set_good_food(self, good_food):
        self.good_Food = good_food
    def get_good_food(self):
        return self.good_Food
    def add_good_food(self, food):
        self.good_Food.append(food)
    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    def likes(self,food):
        return food in self.good_Food

expert = FoodExpert()   
while True:
    option = input('Please enter what you like to do (Q)uit, (N)ame, (D)isplay expert info, (A)dd food, see if an expert (L)ikes a food: ')

    if len(option) > 0 and option[0].lower()== 'q':break
    elif len(option) > 0 and option[0].lower()== 'n':
        name = input('Please enter name of expert: ')
        expert.set_name(name)
    elif len(option) > 0 and option[0].lower() == "d":
        print(f"Name is {expert.get_name()}")
        print(f"Prefered foods in order: {expert.get_good_food()}")
    elif len(option) > 0 and option[0].lower() == "a":
        food = input('Please enter food to add: ')
        expert.add_good_food(food)
    elif len(option) > 0 and option[0].lower() == "l":
        food = input('Please enter food to check: ')
        if expert.likes(food):
            print(f"{expert.get_name()} likes the same food!")
        else:
            print(f"{expert.get_name()} does not like that food :()")

# instantiate an expert
expert1 = FoodExpert() # Runs __init__ method to initialize items.
expert1.set_good_food(['Kale', 'Gumbo', 'Tacos'])
expert1.set_name("Tula Lula")
expert2 = FoodExpert()
expert2.set_good_food(['Salad', 'StirFry', 'Soup'])
expert2.set_name("Pearl Lerl")

print(expert1.get_name(),expert1.get_good_food())
print(expert2.get_name(),expert2.get_good_food())